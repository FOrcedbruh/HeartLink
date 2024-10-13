"""add stage field to profile Table

Revision ID: 04d419d9d281
Revises: 0d8609975950
Create Date: 2024-10-12 11:43:30.111117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04d419d9d281'
down_revision: Union[str, None] = '0d8609975950'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('currentStage', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'currentStage')
    # ### end Alembic commands ###
