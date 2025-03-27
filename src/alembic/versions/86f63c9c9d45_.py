"""empty message

Revision ID: 86f63c9c9d45
Revises: 
Create Date: 2025-03-27 03:58:52.853641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86f63c9c9d45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('walletinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wallet_id', sa.String(length=34), nullable=False),
    sa.Column('trx_balance', sa.DECIMAL(), nullable=True),
    sa.Column('energy_limit', sa.Integer(), nullable=True),
    sa.Column('free_net_limit', sa.Integer(), nullable=True),
    sa.Column('net_limit', sa.Integer(), nullable=True),
    sa.Column('free_net_used', sa.Integer(), nullable=True),
    sa.Column('net_used', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_walletinfo_id'), 'walletinfo', ['id'], unique=False)
    op.create_index(op.f('ix_walletinfo_wallet_id'), 'walletinfo', ['wallet_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_walletinfo_wallet_id'), table_name='walletinfo')
    op.drop_index(op.f('ix_walletinfo_id'), table_name='walletinfo')
    op.drop_table('walletinfo')
    # ### end Alembic commands ###
