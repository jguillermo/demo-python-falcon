# -*- coding: utf-8 -*-
"""create model table

Revision ID: 51532a23a250
Revises: 7143c76037d1
Create Date: 2018-04-09 21:34:09.379659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51532a23a250'
down_revision = '7143c76037d1'
branch_labels = None
depends_on = None

modelTable = 'model'
projectTable = 'project'
operationTypeTable = 'operationType'
propertyTypeTable = 'propertyType'
stageTable = 'stage'


def upgrade():
    op.create_table(
        modelTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idProject', sa.Integer, sa.ForeignKey(projectTable + '.id', name='fk_modelProject'), nullable=False),
        sa.Column('idOperationType', sa.Integer, sa.ForeignKey(operationTypeTable + '.id', name='fk_modelOperationType'),
                  nullable=False),
        sa.Column('idPropertyType', sa.Integer, sa.ForeignKey(propertyTypeTable + '.id', name='fk_modelPropertyType'),
                  nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('bedroom', sa.Integer),
        sa.Column('bathroom', sa.Integer),
        sa.Column('halfBathroom', sa.Integer),
        sa.Column('totalArea', sa.DECIMAL(10, 2)),
        sa.Column('view', sa.Integer, comment='1:Frente,2:Contrafrente,3:Interno,4:Lateral,5:Esquina'),
        sa.Column('unity', sa.Integer),
        sa.Column('floor', sa.Integer),
        sa.Column('garage', sa.Integer),
        sa.Column('price', sa.DECIMAL(10, 2)),
        sa.Column('currency', sa.SmallInteger, server_default='1', comment='1:PEN,2:USD'),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )


def downgrade():
    op.drop_table(modelTable)
