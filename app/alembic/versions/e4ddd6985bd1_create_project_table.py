# -*- coding: utf-8 -*-
"""create project table

Revision ID: e4ddd6985bd1
Revises: b8bd2e2ab4f4
Create Date: 2018-04-09 21:19:44.349264

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4ddd6985bd1'
down_revision = 'b8bd2e2ab4f4'
branch_labels = None
depends_on = None

projectTable = 'project'
propertyTypeTable = 'propertyType'
stageTable = 'stage'


def upgrade():
    op.create_table(
        projectTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idPropertyType', sa.Integer, sa.ForeignKey(propertyTypeTable + '.id', name='fk_projectPropertyType'),
                  nullable=False),
        sa.Column('idStage', sa.Integer, sa.ForeignKey(stageTable + '.id', name='fk_projectStage'), nullable=False,
                  server_default='1'),
        sa.Column('idProfile', sa.Integer, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('idDepartment', sa.Integer, nullable=False),
        sa.Column('idProvince', sa.Integer, nullable=False),
        sa.Column('idDistrict', sa.Integer, nullable=False),
        sa.Column('idUrbanization', sa.Integer, nullable=True),
        sa.Column('idBeach', sa.Integer, nullable=True),
        sa.Column('address', sa.String(255), nullable=False),
        sa.Column('reference', sa.String(255), nullable=True),
        sa.Column('description', sa.Text, nullable=False),
        sa.Column('finished', sa.Text, nullable=True),
        sa.Column('towers', sa.SmallInteger, nullable=True, comment='Cantidad de torres'),
        sa.Column('floors', sa.SmallInteger, nullable=True, comment='Nro de pisos'),
        sa.Column('units', sa.SmallInteger, nullable=True, comment='Total de unidades'),
        sa.Column('elevators', sa.SmallInteger, nullable=True, comment='Total de ascensores'),
        sa.Column('garages', sa.SmallInteger, nullable=True, comment='Nro de cocheras'),
        sa.Column('dateDelivery', sa.DateTime, nullable=True, comment='Fecha entrega'),
        sa.Column('datePublication', sa.DateTime, nullable=False, comment='Fecha publicación'),
        sa.Column('dateExpire', sa.DateTime, nullable=False, comment='Fecha expiración'),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )


def downgrade():
    op.drop_table(projectTable)
