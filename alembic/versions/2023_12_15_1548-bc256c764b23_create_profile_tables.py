"""create profile tables

Revision ID: bc256c764b23
Revises: 40b9e69079c8
Create Date: 2023-12-15 15:48:50.556281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bc256c764b23"
down_revision: Union[str, None] = "40b9e69079c8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profile",
        sa.Column("first_name", sa.String(length=40), nullable=True),
        sa.Column("last_name", sa.String(length=40), nullable=True),
        sa.Column("bio", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("profile")
    # ### end Alembic commands ###
