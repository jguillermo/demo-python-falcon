# -*- coding: utf-8 -*-

import falcon

from bootstrap.container import AppServicesInjector

label = 'message'


class HomeCollectionHandler(object):
    service = AppServicesInjector.home()

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        try:
            response = self.service.highlight()
            resp.media = response
            resp.status = falcon.HTTP_200
        except Exception as e:
            resp.media = {label: str(e)}
            resp.status = falcon.HTTP_500
