import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from src.main import app
from src.app.core.base import Base

engine = create_engine('sqlite:///./test.db')


@pytest.fixture
async def db_session(engine):
    async with sessionmaker(engine, class_=AsyncSession)() as session:
        yield session
        await session.rollback()


@pytest.fixture(scope='module')
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope='module')
def client(test_db):
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope='module')
def test_wallet_id():
    return 'TXo4eRamGwY31gNFkDqLRTWWMjRoQ6ZwrR'


@pytest.fixture(scope='module')
def test_account_info(test_wallet_id):
    return {
        'wallet_id': test_wallet_id,
        'trx_balance': 500,
        'energy_limit': 1000,
        'free_net_limit': 1500,
        'net_limit': 2000,
        'free_net_used': 2500,
        'net_used': 3000,
    }
