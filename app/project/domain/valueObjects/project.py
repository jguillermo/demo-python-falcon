# -*- coding: utf-8 -*-
from project.domain.valueObjects import is_null, validate_date


class Id:
    def __init__(self, id):
        self.value = id


class Name:
    def __init__(self, name):
        if is_null(name):
            raise ValueError('Name: Campo obligatorio')
        else:
            self.value = name


class Description:
    def __init__(self, description):
        if is_null(description):
            raise ValueError('Description: Campo obligatorio')
        else:
            self.value = description


class DateDelivery:
    def __init__(self, date):
        if validate_date(date):
            self.value = date
        else:
            raise ValueError('Fecha inválida')
