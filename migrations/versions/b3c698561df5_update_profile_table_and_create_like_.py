"""Update profile Table and create Like Table

Revision ID: b3c698561df5
Revises: b8e479ececc6
Create Date: 2024-09-09 21:46:50.639642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b3c698561df5'
down_revision: Union[str, None] = 'b8e479ececc6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('liked_profilke_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['liked_profilke_id'], ['profiles.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('profiles', 'followers')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('followers', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=True))
    op.drop_table('likes')
    # ### end Alembic commands ###
