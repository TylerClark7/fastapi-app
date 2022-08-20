"""add user table

Revision ID: 427364ed1aa6
Revises: 2354f1289d14
Create Date: 2022-08-19 00:21:37.025036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '427364ed1aa6'
down_revision = '2354f1289d14'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
              sa.Column('id',sa.Integer(),nullable=False),
              sa.Column('email',sa.String(), nullable=False),
              sa.Column('password', sa.String(), nullable=False),
              sa.Column('created at', sa.TIMESTAMP(timezone=True),
                        server_default=sa.text('now()'), nullable=False),
              sa.PrimaryKeyConstraint('id'),
              sa.UniqueConstraint('email')
              )
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
