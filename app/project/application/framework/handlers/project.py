# -*- coding: utf-8 -*-

from bootstrap.container import AppServicesInjector
from .base import BaseCollectionHandler, BaseHandler


class ProjectCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.project()


class ProjectHandler(BaseHandler):
    service = AppServicesInjector.project()
