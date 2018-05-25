# -*- coding: utf-8 -*-

from project.domain.entities.multimedia import Multimedia
from project.domain.valueObjects.multimedia import Id, Name, Url, Type, State


state_active = 1

class MultimediaFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if 'id' in kwargs else id)
        name = Name(kwargs['name'])
        url = Url(kwargs['url'])
        type = Type(kwargs['type'])
        state = State(kwargs['state'] if 'state' in kwargs else state_active)

        return Multimedia(id.value, name.value, url.value, type.value, state.value)
