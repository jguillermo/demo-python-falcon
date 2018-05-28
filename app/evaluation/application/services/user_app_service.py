from evaluation.application.command.user_command_query import UpdateUserCommand, CreateUserCommand, FindUserQuery
from evaluation.domain.user import UserFactory, UserName, UserLastName
from evaluation.domain.user_repository import UserFinderRepository, UserMngRepository
from evaluation.domain.user_service import UserFinderService


class UserFinderdAppService:
    def __init__(self, user_finder_repository: UserFinderRepository):
        self.user_finder_service = UserFinderService(user_finder_repository)

    def find_by_id(self, query: FindUserQuery):
        user = self.user_finder_service.find_by_id(query.id)
        return {
            'id': user.id,
            'name': user.name,
            'last_name': user.last_name
        }


class UserCreateAppService:
    def __init__(self, user_mng_repository: UserMngRepository):
        self.user_mng_repository = user_mng_repository

    def create(self, command: CreateUserCommand):
        user = UserFactory.create(command.id, command.name, command.last_name)
        self.user_mng_repository.persist(user)
        return True


class UserUpdateAppService:
    def __init__(self, user_mng_repository: UserMngRepository, user_finder_repository: UserFinderRepository):
        self.user_mng_repository = user_mng_repository
        self.user_finder_service = UserFinderService(user_finder_repository)

    def update(self, command: UpdateUserCommand):
        vo_name = UserName(command.name)
        vo_last_name = UserLastName(command.last_name)

        vo_name.validate()
        vo_last_name.validate()

        user = self.user_finder_service.find_by_id(command.id)
        user.name = vo_name.value()
        user.last_name = vo_last_name.value()
        self.user_mng_repository.persist(user)
        return True
