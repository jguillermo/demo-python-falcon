import unittest
from unittest import mock

from evaluation.application.command.user_command_query import FindUserQuery, CreateUserCommand, UpdateUserCommand
from evaluation.application.services.user_app_service import UserFinderdAppService, UserCreateAppService, \
    UserUpdateAppService
from evaluation.domain.user import User
from evaluation.domain.user_repository import UserFinderRepository, UserMngRepository
from sdk.exception import RepositoryNotFound


class UserMockRepository:
    @staticmethod
    def finder(find_by_id_error=False):
        repository = mock.create_autospec(UserFinderRepository)
        repository.find_by_id.return_value = User('123', 'jose', 'guillermo')
        if find_by_id_error:
            repository.find_by_id.return_value = None
        return repository

    @staticmethod
    def mng():
        repository = mock.create_autospec(UserMngRepository)
        repository.persist.return_value = True
        return repository


class TestUserFinderService(unittest.TestCase):

    def test_user_find_by_id_ok(self):
        service = UserFinderdAppService(UserMockRepository.finder())
        finder_user_query = FindUserQuery('123')
        user = service.find_by_id(finder_user_query)
        self.assertEqual('123', user['id'])

    def test_user_find_by_id_error(self):
        service = UserFinderdAppService(UserMockRepository.finder(find_by_id_error=True))
        finder_user_query = FindUserQuery('123')
        with self.assertRaises(RepositoryNotFound):
            service.find_by_id(finder_user_query)


class TestUserCreateService(unittest.TestCase):

    def test_user_create_ok(self):
        service = UserCreateAppService(UserMockRepository.mng())
        create_user_command = CreateUserCommand('123', 'jose', 'guillermo')
        status = service.create(create_user_command)
        self.assertEqual(True, status)


class TestUserUpdateService(unittest.TestCase):

    def test_user_update_ok(self):
        service = UserUpdateAppService(UserMockRepository.mng(),UserMockRepository.finder())
        update_user_command = UpdateUserCommand('123', 'jose', 'guillermo')
        status = service.update(update_user_command)
        self.assertEqual(True, status)

    def test_user_update_error(self):
        service = UserUpdateAppService(UserMockRepository.mng(), UserMockRepository.finder(find_by_id_error=True))
        with self.assertRaises(RepositoryNotFound):
            update_user_command = UpdateUserCommand('123', 'jose', 'guillermo')
            service.update(update_user_command)

