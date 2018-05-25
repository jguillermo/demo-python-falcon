# -*- coding: utf-8 -*-
"""create highlight table

Revision ID: 0d05765534b9
Revises: 58de9b96fd59
Create Date: 2018-04-09 21:24:21.287995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d05765534b9'
down_revision = '58de9b96fd59'
branch_labels = None
depends_on = None

highlightTable = 'highlight'
projectTable = 'project'


def upgrade():
    op.create_table(
        highlightTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idProject', sa.Integer, sa.ForeignKey(projectTable + '.id', name='fk_highlightProject'), nullable=False),
        sa.Column('dateStart', sa.DateTime, nullable=False),
        sa.Column('dateEnd', sa.DateTime, nullable=False),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )


def downgrade():
    op.drop_table(highlightTable)
