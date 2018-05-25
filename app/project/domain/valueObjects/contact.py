# -*- coding: utf-8 -*-

from project.domain.valueObjects import min_max_len, validate_email, is_null, validate_letter, validate_phone_number


class Id(object):
    def __init__(self, id):
        self.value = id


class IdProject(object):
    def __init__(self, project_id):
        self.value = project_id


class Name(object):
    def __init__(self, name, min=3, max=30):
        if min_max_len(name, min, max) and validate_letter(name):
            self.value = name
        else:
            raise ValueError('Name: Min(3) - Max(30) or Invalid characters')


class LastName(object):
    def __init__(self, last_name, min=3, max=30):
        if min_max_len(last_name, min, max) and validate_letter(last_name):
            self.value = last_name
        else:
            raise ValueError('LastName: Min(3) y Max(30) or Invalid characters')


class Phone(object):
    def __init__(self, phone):
        if validate_phone_number(phone) is False:
            raise ValueError('Phone: Between 7 and 9 digits')
        self.value = phone


class PhoneSecond(object):
    def __init__(self, phone_second):
        if phone_second is not None:
            if validate_phone_number(phone_second) is False:
                raise ValueError('PhoneSecond: Between 7 and 9 digits')
        self.value = phone_second


class Schedule(object):
    def __init__(self, schedule, min=1, max=100):
        if is_null(schedule):
            raise ValueError('Schedule: Obligatory field')
        if min_max_len(schedule, min, max) is False:
            raise ValueError('Schedule: Max. Length ' + str(max))
        self.value = schedule


class Email(object):
    def __init__(self, email, min=5, max=50):
        if validate_email(email) is False:
            raise ValueError('Email: Invalid format')
        if min_max_len(email, min, max) is False:
            raise ValueError('Email: Remember Max. Length ' + str(max) + ' characters')
        self.value = email


class EmailGroup(object):
    def __init__(self, email_group, min=5, max=50, max_email=9):
        if email_group is not None:
            email_group = email_group.replace(" ", "")
            emails = email_group.split(';')
            if len(emails) > max_email:
                raise ValueError('EmailGroup: Max 9 emails')
            for email in emails:
                if validate_email(email) is False:
                    raise ValueError('EmailGroup: Invalid format')
                if min_max_len(email, min, max) is False:
                    raise ValueError('EmailGroup: Remember Max. Length ' + str(max) + ' characters')
        self.value = email_group


class State(object):
    def __init__(self, state):
        self.value = state
