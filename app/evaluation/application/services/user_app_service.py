from evaluation.application.input.user_input import UserInput
from evaluation.domain.user import User, UserFactory
from evaluation.domain.user_repository import UserFinderRepository, UserMngRepository
from evaluation.domain.user_service import UserFinderService


class UserFinderdAppService:
    def __init__(self, user_finder_repository: UserFinderRepository) -> None:
        self.user_finder_service = UserFinderService(user_finder_repository)

    def find_by_id(self, id: str) -> User:
        return self.user_finder_service.find_by_id(id)


class UserCreateAppService:
    def __init__(self, user_mng_repository: UserMngRepository) -> None:
        self.user_mng_repository = user_mng_repository

    def create(self, input: UserInput):
        user = UserFactory.create(input)
        self.user_mng_repository.persist(user)
        return True


class UserUpdateCreateAppService:
    def __init__(self, user_mng_repository: UserMngRepository, user_finder_repository: UserFinderRepository) -> None:
        self.user_mng_repository = user_mng_repository
        self.user_finder_service = UserFinderService(user_finder_repository)

    def update(self, id, name, last_name):
        user = self.user_finder_service.find_by_id(id)
        user.name = name
        user.last_name = last_name
        self.user_mng_repository.persist(user)
        return True
