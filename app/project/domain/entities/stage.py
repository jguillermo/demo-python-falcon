# -*- coding: utf-8 -*-

from ..valueObjects.stage import Id, Name, Alias, Type, State


class Stage:
    def __init__(self, id: Id, name: Name, alias: Alias, type: Type, state: State):
        self.id = id.value
        self.name = name.value
        self.alias = alias.value
        self.type = type.value
        self.state = state.value

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
