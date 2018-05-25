# -*- coding: utf-8 -*-
from ..valueObjects.department import Id, Name, Alias, CountryId, Beach, Status


class Department:
    def __init__(self, id: Id, name: Name, alias: Alias, beach: Beach, country_id: CountryId, status: Status):
        self.id = id.value
        self.name = name.value
        self.alias = alias.value
        self.country_id = country_id.value
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
