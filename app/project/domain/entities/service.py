# -*- coding: utf-8 -*-


class Service:
    def __init__(self, id, id_parent, name, alias, level, state):
        self.id = id
        self.idParent = id_parent
        self.name = name
        self.alias = alias
        self.level = level
        self.state = state

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
