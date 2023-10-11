"""create table Question

Revision ID: 0c6b206c9591
Revises: 
Create Date: 2023-10-11 10:48:07.811523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0c6b206c9591'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_question', sa.Integer(), nullable=False),
    sa.Column('text_question', sa.Text(), nullable=False),
    sa.Column('text_answer', sa.Text(), nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('pk', 'id_question'),
    sa.UniqueConstraint('text_question')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    # ### end Alembic commands ###
