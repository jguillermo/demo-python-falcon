# -*- coding: utf-8 -*-
"""create unity table

Revision ID: 9172f40c4c7c
Revises: 51532a23a250
Create Date: 2018-04-09 21:36:16.828431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9172f40c4c7c'
down_revision = '51532a23a250'
branch_labels = None
depends_on = None

unityTable = 'unity'
modelTable = 'model'
stageTable = 'stage'


def upgrade():
    op.create_table(
        unityTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idModel', sa.Integer, sa.ForeignKey(modelTable + '.id', name='fk_unityModel'), nullable=False),
        sa.Column('idStage', sa.Integer, sa.ForeignKey(stageTable + '.id', name='fk_unityStage'), nullable=False,
                  server_default='4'),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('tower', sa.Integer),
        sa.Column('floor', sa.Integer),
        sa.Column('price', sa.DECIMAL(10, 2)),
        sa.Column('currency', sa.SmallInteger, server_default='1', comment='1:PEN,2:USD'),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )


def downgrade():
    op.drop_table(unityTable)
