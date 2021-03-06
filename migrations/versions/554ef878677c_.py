"""empty message

Revision ID: 554ef878677c
Revises: 
Create Date: 2020-07-01 20:29:04.638831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '554ef878677c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('buy', sa.Integer(), nullable=True))
    op.add_column('todo', sa.Column('sell', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'sell')
    op.drop_column('todo', 'buy')
    # ### end Alembic commands ###
