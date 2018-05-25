# -*- coding: utf-8 -*-

from bootstrap.container import AppServicesInjector
from .base import BaseCollectionHandler, BaseHandler


class BankCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.bank()


class BankHandler(BaseHandler):
    service = AppServicesInjector.bank()
