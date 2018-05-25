from evaluation.application.input.user_input import UserInput
from sdk.types import TypeUuid, TypeString


class UserId(TypeUuid):
    pass


class UserName(TypeString):
    pass


class UserLastName(TypeString):
    pass


class User:
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name


class UserFactory:
    @staticmethod
    def create(input: UserInput) -> User:
        id = UserId(input.id)
        name = UserName(input.name)
        last_name = UserLastName(input.last_name)
        UserFactory._validate(id, name, last_name)
        return User(id.value(), name.value(), last_name.value())

    @staticmethod
    def _validate(**value_object):
        for vo in value_object:
            vo.validate()

