from sdk.types import TypeUuid, TypeString, TypeBase


class UserId(TypeUuid):
    pass


class UserName(TypeString):

    def validate(self):
        super().validate()
        if self._value.__len__() < 3:
            raise Exception("El nombre debe ser mayor a 2 caracteres")


class UserLastName(TypeString):
    pass


class User:
    def __init__(self, id, name, last_name):
        self.id = id
        self.name = name
        self.last_name = last_name


class UserFactory:
    @staticmethod
    def create(id,name,last_name) -> User:
        id = UserId(id)
        name = UserName(name)
        last_name = UserLastName(last_name)
        UserFactory._validate([id, name, last_name])
        return User(id.value(), name.value(), last_name.value())

    @staticmethod
    def _validate(value_object):
        for vo in value_object:  # type: TypeBase
            vo.validate()
