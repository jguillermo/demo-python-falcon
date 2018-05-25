# -*- coding: utf-8 -*-

from .base import BaseHandler
from bootstrap.container import AppServicesInjector


class ContactPersistsHandler(BaseHandler):
    service = AppServicesInjector.contact_persists()
