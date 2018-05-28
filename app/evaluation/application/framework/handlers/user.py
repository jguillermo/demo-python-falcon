# -*- coding: utf-8 -*-
import falcon

from bootstrap.container import AppServicesInjector
from evaluation.application.command.user_command_query import CreateUserCommand, UpdateUserCommand, FindUserQuery
from sdk.adapter.log.logging import ConsoleLogger
from sdk.adapter.response.orbis import Response
from sdk.types import TypeUuid


class UserHandler:
    response = Response()

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        try:
            id = TypeUuid.random().value()
            user_create_command = CreateUserCommand(
                id=id,
                name=req.media.get('name', ''),
                last_name=req.media.get('last_name', ''))
            AppServicesInjector.user_create().create(user_create_command)
            resp.media = self.response.success({'id': id})
            resp.status = falcon.HTTP_201
        except Exception as e:
            logger = ConsoleLogger()
            logger.output.error('=== Handler exception ===')
            logger.output.error(str(e), exc_info=True)
            logger.output.error('=' * 25)
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500


class UserIdHandler:
    response = Response()

    def on_get(self, req: falcon.Request, resp: falcon.Response, id):
        try:

            find_user_query = FindUserQuery(id)
            resp.media = self.response.success(AppServicesInjector.user_finder().find_by_id(find_user_query))
            resp.status = falcon.HTTP_200
        except Exception as e:
            print(e.__str__())
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500

    def on_put(self, req: falcon.Request, resp: falcon.Response, id):
        try:
            user_update_command = UpdateUserCommand(
                id=id,
                name=req.media.get('name', ''),
                last_name=req.media.get('last_name', ''))

            AppServicesInjector.user_update().update(user_update_command)
            resp.media = self.response.success('ok')
            resp.status = falcon.HTTP_200
        except Exception as e:
            print(e.__str__())
            resp.media = self.response.error(e.__str__())
            resp.status = falcon.HTTP_500
