"""Renaming students to scholars

Revision ID: b1f8e89461e8
Revises: 791279dd0760
Create Date: 2023-09-04 08:00:45.300508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1f8e89461e8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')