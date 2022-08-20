"""Add foreign key to posts table

Revision ID: 98718fd3778a
Revises: 427364ed1aa6
Create Date: 2022-08-19 16:04:17.724896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98718fd3778a'
down_revision = '427364ed1aa6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    #Owner Id will be in post table and it will get the id number from the 'ID' column in the user table
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')

    pass
