# -*- coding: utf-8 -*-
"""create bankProject table

Revision ID: d12b33ef5ec9
Revises: 0d05765534b9
Create Date: 2018-04-09 21:26:07.645575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd12b33ef5ec9'
down_revision = '0d05765534b9'
branch_labels = None
depends_on = None

bankTable = 'bank'
projectTable = 'project'
bankProjectTable = 'bankProject'


def upgrade():
    op.create_table(
        bankProjectTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idProject', sa.Integer, sa.ForeignKey(projectTable + '.id', name='fk_bankProjectProject'), ),
        sa.Column('idBank', sa.Integer, sa.ForeignKey(bankTable + '.id', name='fk_bankProjectBank')),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )


def downgrade():
    op.drop_table(bankProjectTable)
