"""create servicePropertyType table

Revision ID: ebcd198adeb6
Revises: 44d2605e4804
Create Date: 2018-05-08 23:03:07.024309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebcd198adeb6'
down_revision = '44d2605e4804'
branch_labels = None
depends_on = None

servicePropertyTypeTable = 'servicePropertyType'
serviceTable = 'service'
propertyTypeTable = 'propertyType'


def upgrade():
    table = op.create_table(
        servicePropertyTypeTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idPropertyType', sa.Integer, sa.ForeignKey(propertyTypeTable + '.id', name='fk_servicePropertyTypePropertyType'), nullable=False),
        sa.Column('idService', sa.Integer, sa.ForeignKey(serviceTable + '.id', name='fk_servicePropertyTypeService'), nullable=False),
    )

    op.bulk_insert(
        table,
        [
            {'idPropertyType': 1, 'idService': 2},
            {'idPropertyType': 1, 'idService': 3},
            {'idPropertyType': 1, 'idService': 4},
            {'idPropertyType': 1, 'idService': 5},
            {'idPropertyType': 1, 'idService': 6},
            {'idPropertyType': 1, 'idService': 7},
            {'idPropertyType': 1, 'idService': 10},
            {'idPropertyType': 1, 'idService': 11},
            {'idPropertyType': 1, 'idService': 12},
            {'idPropertyType': 1, 'idService': 13},
            {'idPropertyType': 1, 'idService': 14},
            {'idPropertyType': 1, 'idService': 15},
            {'idPropertyType': 1, 'idService': 16},
            {'idPropertyType': 1, 'idService': 17},
            {'idPropertyType': 1, 'idService': 18},
            {'idPropertyType': 1, 'idService': 19},
            {'idPropertyType': 1, 'idService': 20},
            {'idPropertyType': 1, 'idService': 21},
            {'idPropertyType': 1, 'idService': 22},
            {'idPropertyType': 1, 'idService': 23},
            {'idPropertyType': 1, 'idService': 24},
            {'idPropertyType': 1, 'idService': 25},
            {'idPropertyType': 1, 'idService': 26},
            {'idPropertyType': 1, 'idService': 27},
            {'idPropertyType': 1, 'idService': 28},
            {'idPropertyType': 1, 'idService': 30},
            {'idPropertyType': 1, 'idService': 31},
            {'idPropertyType': 1, 'idService': 32},
            {'idPropertyType': 1, 'idService': 33},
            {'idPropertyType': 1, 'idService': 34},
            {'idPropertyType': 1, 'idService': 35},
            {'idPropertyType': 1, 'idService': 36},
            {'idPropertyType': 1, 'idService': 37},
            {'idPropertyType': 1, 'idService': 38},
            {'idPropertyType': 1, 'idService': 40},
            {'idPropertyType': 1, 'idService': 41},
            {'idPropertyType': 1, 'idService': 42},
            {'idPropertyType': 1, 'idService': 44},
            {'idPropertyType': 1, 'idService': 45},
            {'idPropertyType': 1, 'idService': 46},
            {'idPropertyType': 1, 'idService': 47},
            {'idPropertyType': 1, 'idService': 48},
            {'idPropertyType': 1, 'idService': 49},
            {'idPropertyType': 1, 'idService': 50},
            {'idPropertyType': 1, 'idService': 51},
            {'idPropertyType': 1, 'idService': 52},
            {'idPropertyType': 1, 'idService': 53},
            {'idPropertyType': 1, 'idService': 54},
            {'idPropertyType': 1, 'idService': 55},
            {'idPropertyType': 1, 'idService':  56},
            {'idPropertyType': 15, 'idService': 2},
            {'idPropertyType': 15, 'idService': 3},
            {'idPropertyType': 15, 'idService': 4},
            {'idPropertyType': 15, 'idService': 5},
            {'idPropertyType': 15, 'idService': 6},
            {'idPropertyType': 15, 'idService': 7},
            {'idPropertyType': 15, 'idService': 9},
            {'idPropertyType': 15, 'idService': 14},
            {'idPropertyType': 15, 'idService': 31},
            {'idPropertyType': 15, 'idService': 32},
            {'idPropertyType': 15, 'idService': 33},
            {'idPropertyType': 15, 'idService': 38},
            {'idPropertyType': 15, 'idService': 40},
            {'idPropertyType': 15, 'idService': 41},
            {'idPropertyType': 15, 'idService': 42},
            {'idPropertyType': 15, 'idService': 44},
            {'idPropertyType': 15, 'idService': 45},
            {'idPropertyType': 15, 'idService': 46},
            {'idPropertyType': 15, 'idService': 47},
            {'idPropertyType': 15, 'idService': 48},
            {'idPropertyType': 15, 'idService': 49},
            {'idPropertyType': 15, 'idService': 50},
            {'idPropertyType': 15, 'idService': 51},
            {'idPropertyType': 15, 'idService': 52},
            {'idPropertyType': 15, 'idService': 53},
            {'idPropertyType': 15, 'idService': 54},
            {'idPropertyType': 15, 'idService': 55},
            {'idPropertyType': 15, 'idService': 56},
            {'idPropertyType': 18, 'idService': 2},
            {'idPropertyType': 18, 'idService': 3},
            {'idPropertyType': 18, 'idService': 30},
            {'idPropertyType': 18, 'idService': 32},
            {'idPropertyType': 18, 'idService': 34},
            {'idPropertyType': 18, 'idService': 35},
            {'idPropertyType': 18, 'idService': 36},
            {'idPropertyType': 18, 'idService': 41},
            {'idPropertyType': 18, 'idService': 44},
            {'idPropertyType': 18, 'idService': 45},
            {'idPropertyType': 18, 'idService': 46},
            {'idPropertyType': 18, 'idService': 47},
            {'idPropertyType': 18, 'idService': 48},
            {'idPropertyType': 18, 'idService': 49},
            {'idPropertyType': 18, 'idService': 50},
            {'idPropertyType': 18, 'idService': 51},
            {'idPropertyType': 18, 'idService': 52},
            {'idPropertyType': 18, 'idService': 53},
            {'idPropertyType': 18, 'idService': 54},
            {'idPropertyType': 18, 'idService': 55},
            {'idPropertyType': 18, 'idService': 56}
        ]
    )


def downgrade():
    op.drop_table(servicePropertyTypeTable)
