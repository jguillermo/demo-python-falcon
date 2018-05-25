# -*- coding: utf-8 -*-

from functools import wraps
from project.infrastructure.adapter.log.logging import ConsoleLogger


def handler_except(method):
    @wraps(method)
    def method_wrapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as e:
            logger = ConsoleLogger()
            logger.output.error('=== Handler exception ===')
            logger.output.error(e)
            logger.output.error('=' * 25)
            return e
    return method_wrapper
