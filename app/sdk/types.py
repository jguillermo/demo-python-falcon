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
        if isinstance(self._value, str):
            raise Exception("El tipo de dato no es un string")

    def value(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self.value()


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
