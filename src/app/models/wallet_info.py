from sqlalchemy import Column, Integer, String, DECIMAL

from app.core.db import Base


class WalletInfo(Base):

    wallet_id = Column(
        String(34),
        nullable=False,
        index=True,
        comment='Уникальный идентификатор кошелька в сети Tron'
    )
    trx_balance = Column(
        DECIMAL(20, 6),
        default=DECIMAL('0'),
        comment='Текущий баланс TRX с точностью до 6 знаков',
    )
    energy_limit = Column(
        Integer,
        default=0,
        comment='Лимит энергии',
    )
    free_net_limit = Column(
        Integer,
        default=0,
        comment='Бесплатный лимит BP',
    )
    net_limit = Column(
        Integer,
        default=0,
        comment='Общий лимит BP',
    )
    free_net_used = Column(
        Integer,
        default=0,
        comment='Использовано бесплатных BP'
    )
    net_used = Column(
        Integer,
        default=0,
        comment='Всего использовано BP'
    )
