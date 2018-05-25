# -*- coding: utf-8 -*-
from ..valueObjects.property_type import Id, Id_Parent,  Name, Level, State


class PropertyType:
    def __init__(self, id: Id, id_parent: Id_Parent, name: Name, level: Level, state: State):
        self.id = id.value
        self.idParent = id_parent.value
        self.name = name.value
        self.level = level.value
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
