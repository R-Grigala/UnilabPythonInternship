"""added role in Users

Revision ID: 4b852a9f38dc
Revises: 
Create Date: 2024-06-03 00:08:43.113797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b852a9f38dc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('_password', sa.String(), nullable=False),
    sa.Column('age', sa.Date(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('nationality', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('product')
    # ### end Alembic commands ###
