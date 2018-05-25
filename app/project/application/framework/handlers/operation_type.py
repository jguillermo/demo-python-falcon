# -*- coding: utf-8 -*-

from .base import BaseCollectionHandler
from bootstrap.container import AppServicesInjector


class OperationTypeCollectionHandler(BaseCollectionHandler):
    service = AppServicesInjector.operation_type()
