import uuid
from abc import ABC, abstractmethod


class TypeBase(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def value(self):
        pass


class TypeString(TypeBase):

    def __init__(self, value: str):
        self._value = value

    def validate(self):
        if not isinstance(self._value, str):
            raise Exception("El tipo de dato no es un string {}".format(self._value))

    def value(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self.value()

    # @staticmethod
    # def create(value):
    #     string = self(value)
    #     string.validate()
    #     return string


class TypeUuid(TypeString):
    def __init__(self, value: str):
        super().__init__(value)

    @staticmethod
    def random():
        return TypeUuid(uuid.uuid4().__str__())

    def validate(self):
        super().validate()
        # aqui va una validacion de uuid
        return True


class TypeInteger(TypeBase):

    def __init__(self, value: int):
        self._value = value

    def validate(self):
        if not isinstance(self._value, int):
            raise Exception('El tipo de dato no es un integer')

    def value(self) -> int:
        return self._value


class TypeList(TypeBase):

    def __init__(self, value: list):
        self._value = value

    def validate(self):
        if not isinstance(self._value, list):
            raise Exception('El tipo de dato no es una lista')

    def value(self) -> list:
        return self._value


class TypeFloat(TypeBase):

    def __init__(self, value: float):
        self._value = value

    def validate(self):
        if self._value == 0:
            pass
        elif not isinstance(self._value, float):
            raise Exception('El tipo de dato no es un decimal')

    def value(self) -> float:
        return self._value
