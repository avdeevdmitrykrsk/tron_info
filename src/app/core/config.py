# Standart lib imports
import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Thirdparty imports
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)


class Settings(BaseSettings):
    """Базовые настройки для микросервиса."""

    DATABASE_URL: str = os.getenv('DATABASE_URL')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: str = os.getenv('DB_PORT')
    TRON_API_KEY: str = os.getenv('TRON_API_KEY')
    TRON_PROVIDER_URL: str = os.getenv('TRON_PROVIDER_URL')

    class Config:
        env_file: str = '.env'

    @property
    def async_database_url(self) -> str:
        """Строка асинхронного подключения к postgres DB."""
        if not self.DATABASE_URL:
            return (
                f'postgresql+asyncpg://'
                f'{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}'
                f'@{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}'
            )
        return self.DATABASE_URL

    @property
    def sync_database_url(self) -> str:
        """Строка синхронного подключения к postgres DB (alembic)."""
        return self.async_database_url.replace(
            'postgresql+asyncpg://', 'postgresql+psycopg2://'
        )
        # return 'sqlite:///wallet_info.db'


def setup_logging():
    """Настройка логгера."""

    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        filename=LOG_DIR / 'app.log', encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


settings = Settings()
