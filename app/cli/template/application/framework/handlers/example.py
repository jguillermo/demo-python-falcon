# -*- coding: utf-8 -*-

from .base import BaseCollectionHandler, BaseHandler
from context.application.services.injector import AppServicesInjector


class ExampleCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.example()


class ExampleHandler(BaseHandler):
    service = AppServicesInjector.example()
