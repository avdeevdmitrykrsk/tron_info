import logging

from fastapi import Depends
from tronpy import AsyncTron
from tronpy.exceptions import AddressNotFound, BadAddress
from tronpy.providers import AsyncHTTPProvider

from src.app.exceptions import InvalidAddress, TronNetworkError, WalletNotFound
from src.app.core.config import settings
from src.app.crud.constants import (
    ENERGY_LIMIT_KEY,
    FREE_NET_LIMIT_KEY,
    FREE_NET_USED_KEY,
    NET_LIMIT_KEY,
    NET_USED_KEY,
)

logger: logging = logging.getLogger(__name__)


class WalletService:
    """Сервис для получения данных о кошельке из сети Tron."""

    def __init__(self, client):
        self.client = client

    DEFAULT_WALLET_VALUE: int = 0

    async def get_account_info(self, wallet_id: str) -> tuple:
        """Формирует необходимую информацию из аккаунта."""

        try:
            logger.info('Получение сведений о trx-балансе.')
            trx_balance = await self.client.get_account_balance(wallet_id)

            logger.info('Получение остальных сведений.')
            resources = await self.client.get_account_resource(wallet_id)

            return {
                'wallet_id': wallet_id,
                'trx_balance': trx_balance,
                'energy_limit': resources.get(
                    ENERGY_LIMIT_KEY, self.DEFAULT_WALLET_VALUE
                ),
                'free_net_limit': resources.get(
                    FREE_NET_LIMIT_KEY, self.DEFAULT_WALLET_VALUE
                ),
                'net_limit': resources.get(
                    NET_LIMIT_KEY, self.DEFAULT_WALLET_VALUE
                ),
                'free_net_used': resources.get(
                    FREE_NET_USED_KEY, self.DEFAULT_WALLET_VALUE
                ),
                'net_used': resources.get(
                    NET_USED_KEY, self.DEFAULT_WALLET_VALUE
                ),
            }

        except BadAddress:
            logger.error(
                'Ошибка при получении данных. Невалидный адрес кошелька'
            )
            raise InvalidAddress('Невалидный адрес кошелька')

        except AddressNotFound:
            logger.error(
                'Ошибка при получении данных. Указанный кошелек не найден'
            )
            raise WalletNotFound('Указанный кошелек не найден')

        except ConnectionError:
            logger.error(
                'Ошибка при получении данных. Ошибка подключения к сети Tron'
            )
            raise TronNetworkError('Ошибка подключения к сети Tron')


async def get_tron_client() -> AsyncTron:
    """Создает Tron-клиента для доступа к сети Tron."""
    provider = AsyncHTTPProvider(
        endpoint_uri=settings.TRON_PROVIDER_URL,
        api_key=settings.TRON_API_KEY,
    )
    return AsyncTron(provider=provider)


async def get_wallet_service(
    client: AsyncTron = Depends(get_tron_client),
) -> WalletService:
    return WalletService(client)
