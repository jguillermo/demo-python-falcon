# -*- coding: utf-8 -*-
from project.domain.valueObjects import is_null


class Id(object):
    def __init__(self, id):
        self.value = id


class Id_Parent(object):
    def __init__(self, id_parent):
        self.value = id_parent


class Name(object):
    def __init__(self, name):
        self.value = name

    def is_null(self):
        if is_null(self.value):
            raise ValueError(type(self).__name__+' cannot null')
        pass


class Level(object):
    def __init__(self, level):
        self.value = level


class State(object):
    def __init__(self, state):
        self.value = state
