# -*- coding: utf-8 -*-

from bootstrap.container import AppServicesInjector
from .base import BaseCollectionHandler, BaseHandler


class PropertyTypeCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.property_type()


class PropertyTypeHandler(BaseHandler):
    service = AppServicesInjector.property_type()
