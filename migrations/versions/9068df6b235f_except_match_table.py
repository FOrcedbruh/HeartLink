"""except match table

Revision ID: 9068df6b235f
Revises: 4da40f612e0d
Create Date: 2024-12-24 11:53:40.340654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9068df6b235f'
down_revision: Union[str, None] = '4da40f612e0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matches')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matches',
    sa.Column('first_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('second_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['first_id'], ['profiles.id'], name='matches_first_id_fkey'),
    sa.ForeignKeyConstraint(['second_id'], ['profiles.id'], name='matches_second_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='matches_pkey')
    )
    # ### end Alembic commands ###
