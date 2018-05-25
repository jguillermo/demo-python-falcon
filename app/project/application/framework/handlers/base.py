# -*- coding: utf-8 -*-
import falcon

from project.application.framework.decorators.service import service_validator
from project.infrastructure.common import url
from project.infrastructure.adapter.response.orbis import Response


class BaseCollectionHandler:
    service = None
    response = Response()

    @service_validator
    def on_get(self, req, resp: falcon.Response):
        try:
            params = url.split_query_string(req.params.items())
            resp.media = self.response.success(self.service.find_all(params))
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500

    @service_validator
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        try:
            kwargs = req.media['metadata']
            resp.media = self.response.success(self.service.create(**kwargs))
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500


class BaseHandler:
    service = None
    response = Response()

    @service_validator
    def on_get(self, req, resp: falcon.Response, id):
        try:
            resp.media = self.response.success(self.service.find_by_id(id))
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500

    @service_validator
    def on_put(self, req: falcon.Request, resp: falcon.Response, id):
        try:
            kwargs = req.media['metadata']
            resp.media = self.response.success(self.service.update(id, **kwargs))
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500

    @service_validator
    def on_delete(self, req, resp: falcon.Response, id):
        try:
            resp.media = self.response.success(self.service.delete(id))
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
