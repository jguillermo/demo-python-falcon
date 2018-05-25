# -*- coding: utf-8 -*-


class ServiceProject:
    def __init__(self, id, idService, idProject):
        self.id = id
        self.idService = idService
        self.idProject = idProject

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
