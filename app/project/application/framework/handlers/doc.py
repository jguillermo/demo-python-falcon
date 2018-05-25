# -*- coding: utf-8 -*-

import falcon

from bootstrap.container import AppServicesInjector


class ProjectDocumentationHandler:
    service = AppServicesInjector.doc()

    def on_get(self, req, resp: falcon.Response):
        resp.body = self.service.show_documentation()
        resp.content_type = falcon.MEDIA_HTML
        resp.status = falcon.HTTP_200
