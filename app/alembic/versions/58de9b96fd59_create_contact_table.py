# -*- coding: utf-8 -*-
"""create contact table

Revision ID: 58de9b96fd59
Revises: e4ddd6985bd1
Create Date: 2018-04-09 21:22:46.484529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58de9b96fd59'
down_revision = 'e4ddd6985bd1'
branch_labels = None
depends_on = None

contactTable = 'contact'
projectTable = 'project'


def upgrade():
    op.create_table(
        contactTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idProject', sa.Integer, sa.ForeignKey(projectTable + '.id', name='fk_contactProject'), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('lastName', sa.String(255), nullable=False),
        sa.Column('phone', sa.String(45), nullable=False),
        sa.Column('phoneSecond', sa.String(45)),
        sa.Column('schedule', sa.String(150)),
        sa.Column('email', sa.String(150)),
        sa.Column('emailGroup', sa.Text),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),

    )


def downgrade():
    op.drop_table(contactTable)
