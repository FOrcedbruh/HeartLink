"""create tables

Revision ID: f6079b7ca042
Revises: 
Create Date: 2024-08-28 11:33:11.207972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6079b7ca042'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(length=12), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.LargeBinary(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('profiles',
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('gender', sa.Enum('MALE', 'FEMALE', 'BOY', 'GIRL', name='genders'), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('profileImage', sa.String(), server_default='', nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_table('users')
    # ### end Alembic commands ###
