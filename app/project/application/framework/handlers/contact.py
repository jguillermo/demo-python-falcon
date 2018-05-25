# -*- coding: utf-8 -*-

from bootstrap.container import AppServicesInjector
from .base import BaseHandler


class ContactHandler(BaseHandler):
    service = AppServicesInjector.contact()
