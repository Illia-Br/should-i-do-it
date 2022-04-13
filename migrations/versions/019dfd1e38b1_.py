"""empty message

Revision ID: 019dfd1e38b1
Revises: 4a7ebf8a3600
Create Date: 2022-04-12 21:30:03.062742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019dfd1e38b1'
down_revision = '4a7ebf8a3600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vote_pro', sa.Integer(), nullable=True),
    sa.Column('vote_against', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
