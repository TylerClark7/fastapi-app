"""Add content to post table

Revision ID: 2354f1289d14
Revises: 5faf55007a87
Create Date: 2022-08-19 00:13:51.851762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2354f1289d14'
down_revision = '5faf55007a87'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'content') 
    #Every time you make a revision you have to write how you will undo it
    
    pass
