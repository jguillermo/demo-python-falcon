# -*- coding: utf-8 -*-
import re
import datetime


def is_null(value):
    return value is None


def min_max_len(value, min, max):
    length = len(value)
    return min <= length <= max


def validate_email(email):
    pattern = '^[a-z0-9][a-z0-9-_\.]+@[a-z0-9][a-z0-9-]+[a-z0-9]\.[a-z0-9]{2,10}(?:\.[a-z]{2,10})?$'
    return True if not_allowed(email) and re.match(pattern, email.lower()) else False


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_letter(string):
    pattern = '^[\p{a-z}\p{áéíóúäëïöüñ\'}\s]+$'
    return True if re.match(pattern, string.lower()) else False


def validate_phone_number(string):
    pattern = '^[\p{0-9}]{7,9}$'
    return True if re.match(pattern, string) else False


def not_allowed(string):
    pattern = '(\.{2,}|-{2,}|_{2,})'
    return False if re.search(pattern, string.lower()) else True
