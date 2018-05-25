# -*- coding: utf-8 -*-

from bootstrap.container import AppServicesInjector
from .base import BaseCollectionHandler, BaseHandler


class MultimediaCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.multimedia()


class MultimediaHandler(BaseHandler):
    service = AppServicesInjector.multimedia()
