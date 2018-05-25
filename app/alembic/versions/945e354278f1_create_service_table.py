# -*- coding: utf-8 -*-
"""create service table

Revision ID: 945e354278f1
Revises: 41dcf6fd7e82
Create Date: 2018-04-09 21:11:49.632872

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '945e354278f1'
down_revision = '41dcf6fd7e82'
branch_labels = None
depends_on = None

serviceTable = 'service'


def upgrade():
    table = op.create_table(
        serviceTable,
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('idParent', sa.Integer, sa.ForeignKey(serviceTable + '.id', name='fk_serviceService'), nullable=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('alias', sa.String(150)),
        sa.Column('level', sa.SmallInteger, nullable=False, server_default='1', comment='Nivel de nodo'),
        sa.Column('dateCreate', sa.DateTime, server_default=sa.sql.expression.text('NOW()'), comment='Fecha creación'),
        sa.Column('dateUpdate', sa.TIMESTAMP, server_default=sa.sql.expression.text('CURRENT_TIMESTAMP'),
                  nullable=False, comment='Fecha actualización'),
        sa.Column('state', sa.SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
    )

    op.bulk_insert(
        table,
        [
            {'id': 1, 'idParent': None, 'name': 'Servicios', 'alias': 'servicios', 'level': 1, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 2, 'idParent': 1, 'name': 'Agua', 'alias': 'agua', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 3, 'idParent': 1, 'name': 'Luz', 'alias': 'luz', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 4, 'idParent': 1, 'name': 'Guardianía', 'alias': 'guardiania', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 5, 'idParent': 1, 'name': 'Servicio de Limpieza', 'alias': 'servicio-limpieza', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 6, 'idParent': 1, 'name': 'Sistema de seguridad', 'alias': 'sistema-seguridad', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 7, 'idParent': 1, 'name': 'Conexión a gas', 'alias': 'conexion-gas', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 8, 'idParent': None, 'name': 'Áreas Comunes', 'alias': 'areas-comunes', 'level': 1, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 9, 'idParent': 8, 'name': 'Andén de carga y descarga ', 'alias': 'anden-carga-descarga', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 10, 'idParent': 8, 'name': 'Área de BBQ', 'alias': 'area-bbq', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 11, 'idParent': 8, 'name': 'Área de sauna', 'alias': 'area-sauna', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 12, 'idParent': 8, 'name': 'Área deportiva', 'alias': 'area-deportiva', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 13, 'idParent': 8, 'name': 'Áreas verdes', 'alias': 'areas-verdes', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 14, 'idParent': 8, 'name': 'Cocheras de visitas', 'alias': 'cocheras-visitas', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 15, 'idParent': 8, 'name': 'Gimnasio', 'alias': 'gimnasio', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 16, 'idParent': 8, 'name': 'Guardería', 'alias': 'guarderia', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 17, 'idParent': 8, 'name': 'Jardín', 'alias': 'jardin', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 18, 'idParent': 8, 'name': 'Jardín Paisajista', 'alias': 'jardin-paisajista', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 19, 'idParent': 8, 'name': 'Juegos para niños', 'alias': 'juego-para-niños', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 20, 'idParent': 8, 'name': 'Lavandería de uso común', 'alias': 'lavanderia-uso-comun', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 21, 'idParent': 8, 'name': 'Parque interno', 'alias': 'parque-interno', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 22, 'idParent': 8, 'name': 'Piscina', 'alias': 'piscina', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 23, 'idParent': 8, 'name': 'Sala de cine', 'alias': 'sala-cine', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 24, 'idParent': 8, 'name': 'Sala de internet', 'alias': 'sala-internet', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 25, 'idParent': 8, 'name': 'Salón de Usos Múltiples', 'alias': 'salon-usos-multiples', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 26, 'idParent': 8, 'name': 'Solarium', 'alias': 'solarium', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 27, 'idParent': 8, 'name': 'Club House', 'alias': 'club-house', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 28, 'idParent': 8, 'name': 'Hall de ingreso', 'alias': 'hall-ingreso', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 29, 'idParent': None, 'name': 'Generales', 'alias': 'generales', 'level': 1, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 30, 'idParent': 29, 'name': 'Acceso asfaltado', 'alias': 'acceso-asfaltado', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 31, 'idParent': 29, 'name': 'Centros comerciales cercanos', 'alias': 'centros-comerciales-cercanos', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 32, 'idParent': 29, 'name': 'Acceso para discapacitados', 'alias': 'acceso-para-discapacitados', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 33, 'idParent': 29, 'name': 'Vista a la calle', 'alias': 'vista-calle', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 34, 'idParent': 29, 'name': 'Cerca al mar', 'alias': 'cerca-mar', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 35, 'idParent': 29, 'name': 'Parques cercanos', 'alias': 'parques-cercanos', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 36, 'idParent': 29, 'name': 'Colegios cercanos', 'alias': 'colegios-cercanos', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 37, 'idParent': 29, 'name': 'Frente al mar', 'alias': 'frente-mar', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 38, 'idParent': 29, 'name': 'Antisísmico', 'alias': 'antisismico', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 39, 'idParent': None, 'name': 'Adicionales', 'alias': 'adicionales', 'level': 1, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 40, 'idParent': 39, 'name': 'Cerco eléctrico', 'alias': 'cerco-electrico', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 41, 'idParent': 39, 'name': 'Desagüe', 'alias': 'desague', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 42, 'idParent': 39, 'name': 'Intercomunicador', 'alias': 'intercomunicador', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 43, 'idParent': None, 'name': 'Autorizaciones', 'alias': 'autorizaciones', 'level': 1, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 44, 'idParent': 43, 'name': 'Autorización municipal', 'alias': 'autorizacion-municipal', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 45, 'idParent': 43, 'name': 'Proceso de titulación ', 'alias': 'proceso-titulacion', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 46, 'idParent': 43, 'name': 'Habilitación urbana', 'alias': 'habilitacion-urbana', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 47, 'idParent': 43, 'name': 'Inscripción registral', 'alias': 'inscripcion-registral', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 48, 'idParent': 43, 'name': 'Declaratoria de fábrica', 'alias': 'declaratoria-fabrica', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 49, 'idParent': 43, 'name': 'Declaratoria de edificación ', 'alias': 'declaratoria-edificacion', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 50, 'idParent': 43, 'name': 'Saneamiento', 'alias': 'saneamiento', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 51, 'idParent': 43, 'name': 'Reglamento Interno', 'alias': 'reglamento-interno', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 52, 'idParent': 43, 'name': 'independización ', 'alias': 'independizacion', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 53, 'idParent': 43, 'name': 'Período de garantía', 'alias': 'periodo-garantia', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 54, 'idParent': 43, 'name': 'Central de Informaciones ', 'alias': 'central-informaciones', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 55, 'idParent': 43, 'name': 'Central de Post-venta', 'alias': 'central-post-venta', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
            {'id': 56, 'idParent': 43, 'name': 'Acabados', 'alias': 'acabados', 'level': 2, 'dateCreate': datetime.datetime.utcnow(), 'dateUpdate': datetime.datetime.utcnow(), 'state': 1},
        ]
    )


def downgrade():
    op.drop_table(serviceTable)
