# -*- coding: utf-8 -*-

from bootstrap.container import AppServicesInjector
from .base import BaseCollectionHandler, BaseHandler


class StageCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.stage()


class StageHandler(BaseHandler):
    service = AppServicesInjector.stage()
