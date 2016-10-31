"""empty message

Revision ID: 6b31f9a8fb66
Revises: 334357454f19
Create Date: 2016-10-31 09:54:56.223000

"""

# revision identifiers, used by Alembic.
revision = '6b31f9a8fb66'
down_revision = '334357454f19'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_valid_registered', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_valid_registered')
    ### end Alembic commands ###
