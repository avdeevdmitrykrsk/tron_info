from sqlalchemy import Column, Integer, String, DECIMAL

from src.app.core.db import Base


class WalletInfo(Base):

    wallet_id = Column(String(34), nullable=False, index=True)
    trx_balance = Column(DECIMAL)
    energy_limit = Column(Integer)
    free_net_limit = Column(Integer)
    net_limit = Column(Integer)
    free_net_used = Column(Integer)
    net_used = Column(Integer)
