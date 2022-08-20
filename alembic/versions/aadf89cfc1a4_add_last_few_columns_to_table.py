"""add last few columns to table

Revision ID: aadf89cfc1a4
Revises: 98718fd3778a
Create Date: 2022-08-19 17:58:28.183394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aadf89cfc1a4'
down_revision = '98718fd3778a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('NOW()')),)

    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')

    pass
