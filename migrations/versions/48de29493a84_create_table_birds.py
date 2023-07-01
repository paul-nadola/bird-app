"""Create table birds

Revision ID: 48de29493a84
Revises: 
Create Date: 2023-07-01 10:29:05.686076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48de29493a84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('birds')
    # ### end Alembic commands ###
