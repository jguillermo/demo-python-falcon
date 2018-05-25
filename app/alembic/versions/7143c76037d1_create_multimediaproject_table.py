# -*- coding: utf-8 -*-
"""create multimediaProject table

Revision ID: 7143c76037d1
Revises: a4b683d50640
Create Date: 2018-04-09 21:31:09.673104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7143c76037d1'
down_revision = 'a4b683d50640'
branch_labels = None
depends_on = None

multimediaProjectTable = 'multimediaProject'
multimediaTable = 'multimedia'
projectTable = 'project'


def upgrade():
    op.create_table(
        multimediaProjectTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idMultimedia', sa.Integer, sa.ForeignKey(multimediaTable + '.id', name='fk_multimediaProjectMultimedia'),
                  nullable=False),
        sa.Column('idProject', sa.Integer, sa.ForeignKey(projectTable + '.id', name='fk_multimediaProjectProject'),
                  nullable=False),
    )


def downgrade():
    op.drop_table(multimediaProjectTable)