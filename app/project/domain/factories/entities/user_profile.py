# -*- coding: utf-8 -*-

from project.domain.entities.user_profile import UserProfile
from project.domain.valueObjects.user_profile import Id, IdUser, ProfileIdType, Status

state_active = 1


class UserProfileFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(kwargs['id'] if id is None else id)
        id_user = IdUser(kwargs['userId'])
        profile_id_type = ProfileIdType(kwargs['profileTypeId'])
        status = Status(kwargs['status'])

        id_user.is_null()

        user_profile = UserProfile(id, id_user, profile_id_type, status)
        user_profile.to_dict(kwargs)
        return user_profile
