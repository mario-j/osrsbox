"""empty message

Revision ID: 60ce21d4f6f1
Revises: 554ef878677c
Create Date: 2020-07-02 22:24:09.952618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60ce21d4f6f1'
down_revision = '554ef878677c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('quantity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'quantity')
    # ### end Alembic commands ###
