# -*- coding: utf-8 -*-

ALIAS_TYPE = {1: 'image', 2: 'video', 3: 'pdf', 4: 'panoramic', 5: 'logo'}
IMAGE_TYPE = 1
PANORAMIC_TYPE = 4
LOGO_TYPE = 5


class Id(object):
    def __init__(self, id):
        self.value = id


class Name(object):
    def __init__(self, name):
        self.value = name


class Url(object):
    def __init__(self, url):
        self.value = url


class Type(object):
    def __init__(self, type):
        self.value = type


class State(object):
    def __init__(self, state):
        self.value = state

