# -*- coding: utf-8 -*-
"""create serviceProject table

Revision ID: a4b683d50640
Revises: d12b33ef5ec9
Create Date: 2018-04-09 21:29:15.707438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4b683d50640'
down_revision = 'd12b33ef5ec9'
branch_labels = None
depends_on = None

serviceProjectTable = 'serviceProject'
serviceTable = 'service'
projectTable = 'project'


def upgrade():
    op.create_table(
        serviceProjectTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idService', sa.Integer, sa.ForeignKey(serviceTable + '.id', name='fk_serviceProjectService'), nullable=False),
        sa.Column('idProject', sa.Integer, sa.ForeignKey(projectTable + '.id', name='fk_serviceProjectProject'), nullable=False),
    )


def downgrade():
    op.drop_table(serviceProjectTable)
