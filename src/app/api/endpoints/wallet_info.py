from logging import getLogger

from fastapi import APIRouter, Depends, status
from fastapi_pagination import Params, Page
from sqlalchemy.orm import Session

from app.services import WalletService, get_wallet_service
from app.core.db import get_async_session
from app.crud.wallet_info import wallet_crud
from app.models.wallet_info import WalletInfo
from app.schemas.wallet_info import WalletInfoSchema, WalletInfoDB

router = APIRouter()
logger = getLogger(__name__)


@router.get(
    '/',
    response_model=Page[WalletInfoDB],
    summary='Получение данных о кошельках',
    description="""
    Получает данные о созданных ранее кошельках,
    trx баланс, energy, bandwidth.
    """,
)
async def get_wallet_info(
    params: Params = Depends(),
    session: Session = Depends(get_async_session),
) -> Page[WalletInfoDB]:
    """Получает записи из БД с пагинацией."""
    logger.info('Get-запрос на получение записей из БД принят.')

    instances = await wallet_crud.get_list(session, params)
    logger.info('Записи успешно получены.')

    return instances


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=WalletInfoDB,
    summary='Создать запись о кошельке',
    description="""
    Создает новую запись с информацией о Tron-кошельке в базе данных.
    Получает актуальный баланс и ресурсы из блокчейна Tron.
    """,
)
async def create_wallet_info(
    wallet_id: WalletInfoSchema,
    session: Session = Depends(get_async_session),
    service: WalletService = Depends(get_wallet_service),
) -> WalletInfo:
    """Создает новую запись о кошельке в БД."""
    logger.info('Post-запрос на создание кошелька в БД получен.')

    logger.info('Получение данных из аккаунта.')
    account_info = await service.get_account_info(wallet_id.wallet_id)
    logger.info('Все необходимые ресурсы получены.')

    logger.info('Начинаю процесс создания записи.')
    instance = await wallet_crud.create(
        session, account_info
    )
    logger.info('Запись успешно создана.')

    return instance
