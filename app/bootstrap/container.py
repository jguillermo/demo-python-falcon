# -*- coding: utf-8 -*-
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from evaluation.application.cqrs.user_handler import FindUserQueryHandler, CreateUserCommandHandler, \
    UpdateUserCommandHandler
from evaluation.application.services.doc import DocumentationAppService
from evaluation.application.services.user_app_service import UserFinderdAppService, UserCreateAppService, \
    UserUpdateAppService
from evaluation.infrastructure.adapter.config.file_config import FileConfig
from evaluation.infrastructure.repository.sqlalchemy.user import UserSqlMngRepository, UserSqlFinderRepository
from sdk.adapter.log.logging import ConsoleLogger
from sdk.adapter.sql.sqlalchemy import SqlAlchemyAdapter, SqlAlchemySession


class LoggerInjector(containers.DeclarativeContainer):
    console = providers.Singleton(ConsoleLogger)


class ConfigInjector(containers.DeclarativeContainer):
    app_config = providers.Singleton(FileConfig)


class AdapterInjector(containers.DeclarativeContainer):
    """
    Adapter
    """
    sql_alchemy_session = providers.Singleton(SqlAlchemySession, config=ConfigInjector.app_config)
    sql_alchemy = providers.Factory(SqlAlchemyAdapter, sql_session=sql_alchemy_session)


class RepositoryInjector(containers.DeclarativeContainer):
    """
    Repository
    """
    user_mng = providers.Singleton(UserSqlMngRepository, adapter=AdapterInjector.sql_alchemy)
    user_finder = providers.Singleton(UserSqlFinderRepository, adapter=AdapterInjector.sql_alchemy)


class AppServicesInjector(containers.DeclarativeContainer):
    """
    Application Services
    """
    doc = providers.Singleton(DocumentationAppService)
    user_finder = providers.Singleton(UserFinderdAppService, user_finder_repository=RepositoryInjector.user_finder)
    user_create = providers.Singleton(UserCreateAppService, user_mng_repository=RepositoryInjector.user_mng)
    user_update = providers.Singleton(UserUpdateAppService, user_mng_repository=RepositoryInjector.user_mng,
                                      user_finder_repository=RepositoryInjector.user_finder)


class HandlerInjector(containers.DeclarativeContainer):
    """
    Handler
    """
    FindUserQuery = providers.Singleton(FindUserQueryHandler, service=AppServicesInjector.user_finder)
    CreateUserCommand = providers.Singleton(CreateUserCommandHandler, service=AppServicesInjector.user_create)
    UpdateUserCommand = providers.Singleton(UpdateUserCommandHandler, service=AppServicesInjector.user_update)
