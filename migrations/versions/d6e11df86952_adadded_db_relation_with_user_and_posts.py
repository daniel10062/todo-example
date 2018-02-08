"""Adadded db relation with user and posts

Revision ID: d6e11df86952
Revises: b6cc237b9624
Create Date: 2018-02-07 09:20:25.902594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6e11df86952'
down_revision = 'b6cc237b9624'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###