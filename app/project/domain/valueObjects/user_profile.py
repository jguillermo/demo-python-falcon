# -*- coding: utf-8 -*-
from project.domain.valueObjects import is_null


class Id(object):
    def __init__(self, id):
        self.value = id


class IdUser(object):
    def __init__(self, id_user):
        self.value = id_user

    def is_null(self):
        if is_null(self.value):
            raise ValueError(type(self).__name__+' cannot null')
        pass


class ProfileIdType(object):
    def __init__(self, profile_id_type):
        self.value = profile_id_type

class Status(object):
    def __init__(self, status):
        self.value = status
