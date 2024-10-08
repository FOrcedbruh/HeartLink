"""Add bio to profile table

Revision ID: 86e63bd46907
Revises: 7cc6ec9fba87
Create Date: 2024-09-03 20:32:10.549220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86e63bd46907'
down_revision: Union[str, None] = '7cc6ec9fba87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('bio', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'bio')
    # ### end Alembic commands ###
