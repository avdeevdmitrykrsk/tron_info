from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    sessionmaker,
)

from src.app.core.config import settings


class PreBase:
    """Базовая модель для классов SQLAlchemy."""

    @declared_attr
    def __tablename__(cls):
        """Генерирует имя таблицы в lowercase."""
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)


Base = declarative_base(cls=PreBase)
engine = create_async_engine(settings.async_database_url)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    """Генерирует асинхронную сессию для работы с БД."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
