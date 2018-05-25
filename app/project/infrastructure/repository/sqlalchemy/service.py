# -*- coding: utf-8 -*-
from project.domain.repository.service import ServiceRepository
from project.domain.entities.service import Service
from project.infrastructure.adapter.sql.sqlalchemy import SqlAlchemyAdapter
from project.domain.entities.service_property_type import ServicePropertyType


class ServiceSqlAlchemyRepository(ServiceRepository):
    SERVICE_PROPERTY_TYPE_FIELD = 'idPropertyType'

    def __init__(self, adapter: SqlAlchemyAdapter):
        self.__adapter = adapter
        self.__adapter.entity = Service

    def find_all(self, params):
        try:
            filters = params['filter']
            service_project_type_filter = {}
            if self.SERVICE_PROPERTY_TYPE_FIELD in filters:
                service_project_type_filter[self.SERVICE_PROPERTY_TYPE_FIELD] = filters[self.SERVICE_PROPERTY_TYPE_FIELD]
                del filters[self.SERVICE_PROPERTY_TYPE_FIELD]

            return self.__adapter.session.query(Service).filter_by(**filters).\
                join(ServicePropertyType, Service.id == ServicePropertyType.idService).\
                filter_by(**service_project_type_filter).\
                all()
        except Exception as e:
            raise e
