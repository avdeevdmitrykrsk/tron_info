from http import HTTPStatus

import pytest
from unittest.mock import AsyncMock

from src.app.models.wallet_info import WalletInfo
from src.app.crud.wallet_info import CRUDWallet

import pytest
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_wallet(test_wallet_id: str, test_account_info: dict):
    """Тест создания записи о кошельке."""
    mock_session = AsyncMock(spec=AsyncSession)
    service = CRUDWallet()

    result = await service.create(
        session=mock_session, account_info=test_account_info
    )

    mock_session.add.assert_called_once()
    mock_session.commit.assert_awaited_once()
    mock_session.refresh.assert_awaited_once()

    assert isinstance(result, WalletInfo)
    assert result.wallet_id == test_wallet_id


def test_get_wallet_info_enpoint(client):
    response = client.get('/api/wallet_info')
    assert response.status_code == HTTPStatus.OK

    response_data = response.json()
    assert 'items' in response_data
    assert isinstance(response_data['items'], list)
