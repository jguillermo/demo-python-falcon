# -*- coding: utf-8 -*-
from ..valueObjects.bank import Id, Name, Abbreviation, Logo, State


class Bank:
    def __init__(self, id: Id, name: Name, abbreviation: Abbreviation, logo: Logo, state: State):
        self.id = id.value
        self.name = name.value
        self.abbreviation = abbreviation.value
        self.logo = logo.value
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
