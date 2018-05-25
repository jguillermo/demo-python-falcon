# -*- coding: utf-8 -*-
from project.domain.factories.entities.user_profile import UserProfileFactory


class UserMicroServiceRepository():

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = UserProfileFactory
        self.__adapter.name_microservice = 'ms_user'
        self.__adapter.name_resource = 'profile'

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e
