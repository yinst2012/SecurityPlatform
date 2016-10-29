"""update user&topic

Revision ID: e32426d3e862
Revises: 5b7e323cd9af
Create Date: 2016-10-29 16:23:09.095000

"""

# revision identifiers, used by Alembic.
revision = 'e32426d3e862'
down_revision = '5b7e323cd9af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('postNum', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('topicNum', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'topicNum')
    op.drop_column('users', 'postNum')
    ### end Alembic commands ###