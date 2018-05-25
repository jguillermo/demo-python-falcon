# -*- coding: utf-8 -*-
"""create serviceModel table

Revision ID: 95233558d792
Revises: 9172f40c4c7c
Create Date: 2018-04-09 21:39:19.855750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95233558d792'
down_revision = '9172f40c4c7c'
branch_labels = None
depends_on = None

serviceModelTable = 'serviceModel'
serviceTable = 'service'
modelTable = 'model'


def upgrade():
    op.create_table(
        serviceModelTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idService', sa.Integer, sa.ForeignKey(serviceTable + '.id', name='fk_serviceModelService'), nullable=False),
        sa.Column('idModel', sa.Integer, sa.ForeignKey(modelTable + '.id', name='fk_serviceModelModel'), nullable=False),
    )


def downgrade():
    op.drop_table(serviceModelTable)
