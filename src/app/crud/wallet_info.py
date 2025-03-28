import logging

from fastapi_pagination import Params, Page
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.wallet_info import WalletInfo

logger: logging = logging.getLogger(__name__)


class CRUDWallet:

    async def create(
        self,
        session: AsyncSession,
        account_info: dict,
    ) -> WalletInfo:
        """Делает запись в БД на основе полученной информации."""
        instance = WalletInfo(**account_info)

        session.add(instance)
        await session.commit()
        await session.refresh(instance)

        return instance

    async def get_list(self, session: AsyncSession, params: Params) -> Page:
        """Получает все записи из БД с пагинацией."""
        logger.info('Получение записей из БД.')
        instances = await paginate(session, select(WalletInfo), params)

        return instances


wallet_crud = CRUDWallet()
