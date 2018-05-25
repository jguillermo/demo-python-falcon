# -*- coding: utf-8 -*-

from project.domain.entities.bank import Bank
from project.domain.valueObjects.bank import Id, Name, Abbreviation, Logo, State

state_active = 1


class BankFactory:

    @staticmethod
    def create(kwargs, id=None):
        id = Id(id)
        name = Name(kwargs['name'])
        abbreviation = Abbreviation(kwargs['abbreviation'])
        logo = Logo(kwargs['logo'])
        state = State(state_active)

        return Bank(id, name, abbreviation, logo, state)
