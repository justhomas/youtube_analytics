"""create tables

Revision ID: a29dc86fd75c
Revises: 
Create Date: 2024-02-14 23:23:17.426000

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a29dc86fd75c"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_category_id"), "category", ["id"], unique=False)
    op.create_table(
        "region",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_region_id"), "region", ["id"], unique=False)
    op.create_table(
        "video",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("video_id", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_video_id"), "video", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_video_id"), table_name="video")
    op.drop_table("video")
    op.drop_index(op.f("ix_region_id"), table_name="region")
    op.drop_table("region")
    op.drop_index(op.f("ix_category_id"), table_name="category")
    op.drop_table("category")
    # ### end Alembic commands ###