import re
from decimal import Decimal

from pydantic import BaseModel, validator


class WalletInfoSchema(BaseModel):
    """Pydantic-схема для получения wallet_id."""

    wallet_id: str

    @validator('wallet_id')
    def validate_account(cls, value: str):
        """ Валидатор поля wallet_id."""
        if not re.match(r'^T[a-km-zA-HJ-NP-Z1-9]{33}$', value):
            raise ValueError(
                'Адрес кошелька должен начинаться с заглавной "T", '
                'иметь длину 34 символа, '
                'не содержать символов "0", "O", "I", "l", '
            )

        return value


class WalletInfoDB(BaseModel):
    """Pydantic-схема для возврата созданного объекта."""

    wallet_id: str
    trx_balance: Decimal
    energy_limit: int
    free_net_limit: int
    net_limit: int
    free_net_used: int
    net_used: int

    class Config:
        orm_mode = True
