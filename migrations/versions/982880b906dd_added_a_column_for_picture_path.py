"""added a column for picture_path

Revision ID: 982880b906dd
Revises: 61a8e0633113
Create Date: 2021-08-29 19:57:01.454709

"""

# revision identifiers, used by Alembic.
revision = '982880b906dd'
down_revision = '61a8e0633113'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###
