# -*- coding: utf-8 -*-
from ..valueObjects.district import Id, Name, Alias, IdDepartment, IdProvince, Beach, Status


class District:
    def __init__(self, id: Id, name: Name, alias: Alias, id_department: IdDepartment, id_province: IdProvince, beach: Beach, status: Status):
        self.id = id.value
        self.name = name.value
        self.alias = alias.value
        self.id_department = id_department.value
        self.id_province = id_province.value
        self.beach = beach.value
        self.status = status.value

    def dispatch(self):
        """Use for send domain events"""
        return self.metadata

    def _record(self, event, queue, action):
        """Use for record a entity event"""
        self.metadata = {
            'event': event,
            'queue': queue,
            'action': action
        }

    def to_dict(self, *args, **kwargs):
        self.dict = dict(*args, **kwargs)
