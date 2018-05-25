# -*- coding: utf-8 -*-
from bootstrap.container import AppServicesInjector
from project.application.framework.handlers.base import BaseCollectionHandler


class ServiceCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.service()

