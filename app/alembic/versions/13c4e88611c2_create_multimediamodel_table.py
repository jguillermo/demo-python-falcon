# -*- coding: utf-8 -*-
"""create multimediaModel table

Revision ID: 13c4e88611c2
Revises: 95233558d792
Create Date: 2018-04-09 21:41:06.470821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13c4e88611c2'
down_revision = '95233558d792'
branch_labels = None
depends_on = None

multimediaModelTable = 'multimediaModel'
multimediaTable = 'multimedia'
modelTable = 'model'


def upgrade():
    op.create_table(
        multimediaModelTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idMultimedia', sa.Integer, sa.ForeignKey(multimediaTable + '.id', name='fk_multimediaModelMultimedia'),
                  nullable=False),
        sa.Column('idModel', sa.Integer, sa.ForeignKey(modelTable + '.id', name='fk_multimediaModelModel'),
                  nullable=False),
    )


def downgrade():
    op.drop_table(multimediaModelTable)
