"""empty message

Revision ID: 38f5cc97bb79
Revises: 
Create Date: 2021-04-09 09:24:40.354211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38f5cc97bb79'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('contacts',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('mail', sa.String(), server_default='', nullable=False),
                    sa.Column('subject', sa.String(), nullable=False),
                    sa.Column('text', sa.String(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    )


def downgrade():
    op.drop_table('contacts')
