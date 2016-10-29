"""add group

Revision ID: acc7a5fd9100
Revises: e8f5265f2666
Create Date: 2016-10-29 15:07:00.588000

"""

# revision identifiers, used by Alembic.
revision = 'acc7a5fd9100'
down_revision = 'e8f5265f2666'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('topicNum', sa.Integer(), nullable=True),
    sa.Column('createdTime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('visitNum', sa.Integer(), nullable=True),
    sa.Column('postNum', sa.Integer(), nullable=True),
    sa.Column('groupID', sa.Integer(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('createdTime', sa.DateTime(), nullable=True),
    sa.Column('updatedTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['groupID'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=1024), nullable=False),
    sa.Column('topicID', sa.Integer(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=True),
    sa.Column('createdTime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['topicID'], ['topics.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('topics')
    op.drop_table('groups')
    ### end Alembic commands ###
