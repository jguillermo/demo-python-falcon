# -*- coding: utf-8 -*-


class Contact:
    def __init__(self, project_id, name, last_name, phone, phone_second, schedule, email, email_group, state, id=None):
        self.id = id
        self.idProject = project_id
        self.name = name
        self.lastName = last_name
        self.phone = phone
        self.phoneSecond = phone_second
        self.schedule = schedule
        self.email = email
        self.emailGroup = email_group
        self.state = state
