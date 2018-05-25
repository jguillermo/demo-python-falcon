# -*- coding: utf-8 -*-
"""create propertyType table

Revision ID: c630fa1fbe5a
Revises: 0c991f431dfa
Create Date: 2018-04-09 21:06:52.558941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c630fa1fbe5a'
down_revision = '0c991f431dfa'
branch_labels = None
depends_on = None

propertyTypeTable = 'propertyType'


def upgrade():
    table = op.create_table(
        propertyTypeTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idParent', sa.Integer, sa.ForeignKey(propertyTypeTable + '.id', name='fk_propertyTypePropertyType'),
                  nullable=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('level', sa.SmallInteger, nullable=False, server_default='1', comment='Nivel de nodo'),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )
    op.bulk_insert(
        table,
        [
            {'id': 1, 'name': 'Residencial', 'idParent': None, 'level': 1},
            {'id': 2, 'name': 'Departamentos', 'idParent': 1, 'level': 2},
            {'id': 3, 'name': 'Departamento', 'idParent': 2, 'level': 3},
            {'id': 4, 'name': 'Departamento Duplex', 'idParent': 2, 'level': 3},
            {'id': 5, 'name': 'Departamento Triplex', 'idParent': 2, 'level': 3},
            {'id': 6, 'name': 'Departamento de Playa', 'idParent': 2, 'level': 3},
            {'id': 7, 'name': 'Departamento Loft', 'idParent': 2, 'level': 3},
            {'id': 8, 'name': 'Departamento Penthouse', 'idParent': 2, 'level': 3},
            {'id': 9, 'name': 'Casas', 'idParent': 1, 'level': 2},
            {'id': 10, 'name': 'Casa', 'idParent': 9, 'level': 3},
            {'id': 11, 'name': 'Casa de playa', 'idParent': 9, 'level': 3},
            {'id': 12, 'name': 'Casa de playa en condominio', 'idParent': 9, 'level': 3},
            {'id': 13, 'name': 'Casa de campo', 'idParent': 9, 'level': 3},
            {'id': 14, 'name': 'Casa en condominio', 'idParent': 9, 'level': 3},
            {'id': 15, 'name': 'Comercial', 'idParent': None, 'level': 1},
            {'id': 16, 'name': 'Oficinas', 'idParent': 15, 'level': 2},
            {'id': 17, 'name': 'Locales comerciales', 'idParent': 15, 'level': 2},
            {'id': 18, 'name': 'Lotes', 'idParent': None, 'level': 1},
            {'id': 19, 'name': 'Lotes / terrenos', 'idParent': 18, 'level': 2},
        ]
    )


def downgrade():
    op.drop_table(propertyTypeTable)
