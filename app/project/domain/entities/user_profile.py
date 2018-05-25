# -*- coding: utf-8 -*-
from ..valueObjects.user_profile import Id, IdUser, ProfileIdType, Status


class UserProfile:
    def __init__(self, id: Id, id_user: IdUser, profile_id_type: ProfileIdType, status: Status):
        self.id = id.value
        self.id_user = id_user.value
        self.profile_id_type = profile_id_type.value
        self.status = status.value

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

    def to_dict(self, *args, **kwargs):
        self.dict = dict(*args, **kwargs)
