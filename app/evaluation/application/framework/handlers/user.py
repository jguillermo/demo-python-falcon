# -*- coding: utf-8 -*-
import falcon

from evaluation.application.bus.user_command_query import CreateUserCommand, UpdateUserCommand, FindUserQuery
from evaluation.application.framework.decorators.service import handler_except
from evaluation.application.framework.handlers.base import Base
from sdk.types import TypeUuid


class UserHandler(Base):

    @handler_except
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        id = TypeUuid.random().value()
        command = CreateUserCommand(
            id=id,
            name=req.media.get('name', ''),
            last_name=req.media.get('last_name', ''))
        self.command_bus.dispatch(command)
        return {'id': id}


class UserIdHandler(Base):

    @handler_except
    def on_get(self, req: falcon.Request, resp: falcon.Response, id):
        query = FindUserQuery(id)
        return self.command_query.ask(query)

    @handler_except
    def on_put(self, req: falcon.Request, resp: falcon.Response, id):
        command = UpdateUserCommand(
            id=id,
            name=req.media.get('name', ''),
            last_name=req.media.get('last_name', ''))
        self.command_bus.dispatch(command)
        return 'ok'
