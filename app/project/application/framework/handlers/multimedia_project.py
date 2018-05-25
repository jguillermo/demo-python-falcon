# -*- coding: utf-8 -*-
import falcon

from bootstrap.container import AppServicesInjector
from project.application.framework.decorators.service import service_validator
from project.infrastructure.adapter.response.orbis import Response


class MultimediaProjectCollectionHandler:
    service = AppServicesInjector.multimedia_project()
    response = Response()

    @service_validator
    def on_get(self, req, resp: falcon.Response, id):
        try:
            resp.media = self.response.success(self.service.find_by_id_project(id))
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500

    @service_validator
    def on_post(self, req: falcon.Request, resp: falcon.Response, id):
        try:
            kwargs = req.media['metadata']
            resp.media = self.response.success(self.service.create(id, **kwargs))
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500
