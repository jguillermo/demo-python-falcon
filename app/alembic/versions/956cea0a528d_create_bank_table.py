# -*- coding: utf-8 -*-
"""create bank table

Revision ID: 956cea0a528d
Revises:
Create Date: 2018-04-06 20:25:14.108935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '956cea0a528d'
down_revision = None
branch_labels = None
depends_on = None

bankTable = 'bank'


def upgrade():
    table = op.create_table(
        bankTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('abbreviation', sa.String(150), nullable=True),
        sa.Column('logo', sa.String(100)),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )

    op.bulk_insert(
        table,
        [
            {'name': 'Banco de comercio'},
            {'name': 'Banco de Crédito'},
            {'name': 'Banco de la Nación'},
            {'name': 'Banco Falabella'},
            {'name': 'Banco Interamericano de Finanzas'},
            {'name': 'Banco Ripley'},
            {'name': 'Banco Continental'},
            {'name': 'Caja Huancayo'},
            {'name': 'Caja Metropolitana'},
            {'name': 'Caja Piura'},
            {'name': 'Caja Sullana'},
            {'name': 'Cencosud'},
            {'name': 'Financiamiento Propio'},
            {'name': 'GNB'},
            {'name': 'Interbank'},
            {'name': 'Scotiabank'},
        ]
    )


def downgrade():
    op.drop_table(bankTable)
