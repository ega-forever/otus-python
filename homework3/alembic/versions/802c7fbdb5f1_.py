"""empty message

Revision ID: 802c7fbdb5f1
Revises: 
Create Date: 2021-03-16 08:26:31.113737

"""
from alembic import op
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

# revision identifiers, used by Alembic.
revision = '802c7fbdb5f1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'ips',
        Column('id', Integer, primary_key=True),
        Column('country', String(32), unique=False),
        Column('region', String(32), unique=False),
        Column('city', String(32), unique=False),
        Column('zip', String(32), unique=False),
        Column('lat', Float, unique=False),
        Column('lon', Float, unique=False),
        Column('ip', String(32), unique=False)
    )


def downgrade():
    op.drop_table('ips')
