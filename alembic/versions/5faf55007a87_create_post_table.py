"""create post table

Revision ID: 5faf55007a87
Revises: 
Create Date: 2022-08-12 22:09:02.009680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5faf55007a87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))





def downgrade() -> None:
    op.drop_table('posts')
    pass
