# -*- coding: utf-8 -*-
"""create multimedia table

Revision ID: b8bd2e2ab4f4
Revises: 945e354278f1
Create Date: 2018-04-09 21:11:58.465125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8bd2e2ab4f4'
down_revision = '945e354278f1'
branch_labels = None
depends_on = None

multimediaTable = 'multimedia'


def upgrade():
    op.create_table(
        multimediaTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('url', sa.String(255), nullable=False),
        sa.Column('order', sa.Integer, server_default='1', comment='Orden de archivo multimedia'),
        sa.Column('type', sa.SmallInteger, server_default='1', comment='1:Image,2:Video,3:Pdf,4:360'),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )


def downgrade():
    op.drop_table(multimediaTable)
