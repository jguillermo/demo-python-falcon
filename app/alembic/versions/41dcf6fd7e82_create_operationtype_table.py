# -*- coding: utf-8 -*-
"""create operationType table

Revision ID: 41dcf6fd7e82
Revises: c630fa1fbe5a
Create Date: 2018-04-09 21:09:49.067305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41dcf6fd7e82'
down_revision = 'c630fa1fbe5a'
branch_labels = None
depends_on = None

operationType = 'operationType'


def upgrade():
    table = op.create_table(
        operationType,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255)),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )

    op.bulk_insert(
        table,
        [
            {'id': 1, 'name': 'Venta', 'state': 1},
            {'id': 2, 'name': 'Alquiler', 'state': 1},
        ]
    )

def downgrade():
    op.drop_table(operationType)
