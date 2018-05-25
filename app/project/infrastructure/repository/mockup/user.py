# -*- coding: utf-8 -*-
from project.domain.factories.entities.user_profile import UserProfileFactory


class MockUserProfileRepository():

    def __init__(self):
        self.data = [
            {"id": "1", "userId": "62", "profileTypeId": "1", "totalMessages": "0", "totalAnnouncementActives": "0",
             "contactPersistence": None, "contactPersistenceId": None, "status": "1"}
        ]

    def find_by_id(self, id_profile):
        for key, user_profile in enumerate(self.data):
            if user_profile['id'] == id_profile:
                return UserProfileFactory.create(self.data[key])
