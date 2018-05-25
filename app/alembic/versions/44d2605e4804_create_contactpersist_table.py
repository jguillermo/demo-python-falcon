"""create contactpersist table

Revision ID: 44d2605e4804
Revises: 13c4e88611c2
Create Date: 2018-04-30 21:48:30.925089

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '44d2605e4804'
down_revision = '13c4e88611c2'
branch_labels = None
depends_on = None

contactPersistTable = 'contactPersist'
contactTable = 'contact'


def upgrade():
    op.create_table(
        contactPersistTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idContact', sa.Integer, sa.ForeignKey(contactTable + '.id', name='fk_contactPersistContact'), nullable=False),
        sa.Column('idProfile', sa.Integer, nullable=False),
        sa.Column('state', sa.SmallInteger, server_default='0', comment='1:persiste, 0:no')
    )


def downgrade():
    op.drop_table(contactPersistTable)
