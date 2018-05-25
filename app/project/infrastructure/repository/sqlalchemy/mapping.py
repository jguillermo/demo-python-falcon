# -*- coding: utf-8 -*-

from sqlalchemy import MetaData, Table, Column, String, Integer, Text, ForeignKey, DateTime, TIMESTAMP, SmallInteger, sql
from sqlalchemy.orm import mapper, relationship, clear_mappers
from project.domain.entities.project import Project
from project.domain.entities.contact import Contact
from project.domain.entities.service import Service
from project.domain.entities.service_project import ServiceProject
from project.domain.entities.property_type import PropertyType
from project.domain.entities.bank import Bank
from project.domain.entities.stage import Stage
from project.domain.entities.multimedia import Multimedia
from project.domain.entities.contact_persist import ContactPersist
from project.domain.entities.service_property_type import ServicePropertyType
from project.domain.entities.multimedia_project import MultimediaProject
from project.domain.entities.operation_type import OperationType

metadata = MetaData()
project = Table('project', metadata,
                Column('id', Integer, primary_key=True, nullable=False),
                Column('idPropertyType', Integer, nullable=False),
                Column('idStage', Integer, nullable=False, server_default='1'),
                Column('idProfile', Integer, nullable=False),
                Column('name', String(255), nullable=False),
                Column('idDepartment', Integer, nullable=False),
                Column('idProvince', Integer, nullable=False),
                Column('idDistrict', Integer, nullable=False),
                Column('idUrbanization', Integer, nullable=True),
                Column('idBeach', Integer, nullable=True),
                Column('address', String(255), nullable=False),
                Column('reference', String(255), nullable=True),
                Column('description', Text, nullable=False),
                Column('finished', Text, nullable=True),
                Column('towers', SmallInteger),
                Column('floors', SmallInteger),
                Column('units', SmallInteger),
                Column('elevators', SmallInteger),
                Column('garages', SmallInteger),
                Column('dateDelivery', DateTime, nullable=True, comment='Fecha entrega'),
                Column('datePublication', DateTime, nullable=False, comment='Fecha publicación'),
                Column('dateExpire', DateTime, nullable=False, comment='Fecha creación'),
                Column('state', SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado')
                )

contact = Table('contact', metadata,
                Column('id', Integer, primary_key=True, nullable=False),
                Column('idProject', Integer, ForeignKey('project.id')),
                Column('name', String(255)),
                Column('lastName', String(255)),
                Column('phone', String(45)),
                Column('phoneSecond', String(45)),
                Column('schedule', String(150)),
                Column('email', String(100)),
                Column('emailGroup', Text),
                Column('state', SmallInteger)
                )

property_type = Table('propertyType', metadata,
                      Column('id', Integer, primary_key=True, nullable=False),
                      Column('idParent', Integer, nullable=True),
                      Column('name', String(255), nullable=False),
                      Column('level', Integer, nullable=False),
                      Column('state', SmallInteger, nullable=True)
                      )

service = Table('service', metadata,
                Column('id', Integer, primary_key=True, nullable=False),
                Column('idParent', Integer),
                Column('name', String(255)),
                Column('alias', String(150)),
                Column('level', SmallInteger, server_default='1'),
                Column('dateCreate', DateTime, server_default=sql.expression.text('NOW()')),
                Column('dateUpdate', TIMESTAMP, nullable=False),
                Column('state', SmallInteger, server_default='1')
                )

service_project = Table('serviceProject', metadata,
                        Column('id', Integer, primary_key=True, nullable=False),
                        Column('idService', Integer, ForeignKey('service.id')),
                        Column('idProject', Integer, ForeignKey('project.id'))
                        )

bank = Table('bank', metadata,
             Column('id', Integer, primary_key=True, nullable=False),
             Column('name', String(255)),
             Column('abbreviation', String(150)),
             Column('logo', String(100)),
             Column('state', SmallInteger),
             )

stage = Table('stage', metadata,
              Column('id', Integer, primary_key=True, nullable=False),
              Column('name', String(255)),
              Column('alias', String(255), nullable=False),
              Column('type', SmallInteger, nullable=False, server_default='1', comment='1:Proyecto,2:Modelo,3:Unidad'),
              Column('state', SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
              )

multimedia = Table('multimedia', metadata,
                   Column('id', Integer, primary_key=True, nullable=False),
                   Column('name', String(255)),
                   Column('url', String(255)),
                   Column('type', SmallInteger),
                   Column('state', SmallInteger, server_default='1', comment='1:Activo,2:Desactivo,3:Eliminado'),
                   )

contact_persist = Table('contactPersist', metadata,
                        Column('id', Integer, primary_key=True, nullable=False),
                        Column('idContact', Integer, ForeignKey('contact.id')),
                        Column('idProfile', Integer, nullable=False),
                        Column('state', SmallInteger, server_default='0')
                        )

service_property_type = Table('servicePropertyType', metadata,
                              Column('id', Integer, primary_key=True, nullable=False),
                              Column('idPropertyType', Integer, ForeignKey('propertyType.id')),
                              Column('idService', Integer, ForeignKey('service.id')),
                              )

multimedia_project = Table('multimediaProject', metadata,
                           Column('id', Integer, primary_key=True, nullable=False),
                           Column('idMultimedia', Integer, ForeignKey('multimedia.id')),
                           Column('idProject', Integer, ForeignKey('project.id'))
                           )

operation_type = Table('operationType', metadata,
                       Column('id', Integer, primary_key=True, nullable=False),
                       Column('name', String(255)),
                       Column('state', SmallInteger)
                       )


def load_mapper():
    clear_mappers()
    mapper(OperationType, operation_type)
    mapper(Multimedia, multimedia)
    mapper(Stage, stage)
    mapper(Project, project, properties={'Contacts': relationship(Contact, backref='project', order_by=contact.c.id)})
    mapper(Contact, contact)
    mapper(Service, service)
    mapper(PropertyType, property_type)
    mapper(Bank, bank)
    mapper(ServiceProject, service_project)
    mapper(ContactPersist, contact_persist)
    mapper(ServicePropertyType, service_property_type)
    mapper(MultimediaProject, multimedia_project)
