# -*- coding: utf-8 -*-


class Id(object):
    def __init__(self, id):
        self.value = id


class IdParent(object):
    def __init__(self, name):
        self.value = name


class Name(object):
    def __init__(self, name):
        self.value = name


class Alias(object):
    def __init__(self, alias):
        self.value = alias


class Level(object):
    def __init__(self, type):
        self.value = type


class State(object):
    def __init__(self, state):
        self.value = state
