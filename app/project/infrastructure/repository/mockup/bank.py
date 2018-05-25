# -*- coding: utf-8 -*-
from project.domain.repository.bank import BankRepository
from project.domain.entities.bank import Bank
from project.domain.valueObjects.bank import Id, Name, Logo, Abbreviation, State


class MockBankRepository(BankRepository):

    def __init__(self):
        self.data = [
            {"name": "Banco de comercio", "id": 1, "logo": None, "abbreviation": None, "state": 1},
            {"name": "Banco de Crédito", "id": 2, "logo": None, "abbreviation": None, "state": 1},
            {"name": "Banco de la Nación", "id": 3, "logo": None, "abbreviation": None, "state": 1},
            {"name": "Banco Falabella", "id": 4, "logo": None, "abbreviation": None, "state": 1},
        ]

    def create(self, bank: Bank):
        self.data.append(
            {'id': bank.id, 'name': bank.name}
        )
        return True

    def update(self, bank):
        pass

    def delete(self, id):
        pass

    def find_all(self, params=None):
        resp = []
        for bank in self.data:
            id = Id(bank['id'])
            name = Name(bank['name'])
            logo = Logo(bank['logo'])
            abbreviation = Abbreviation(bank['abbreviation'])
            state = State(bank['state'])
            resp.append(Bank(id, name, logo, abbreviation, state))
        return resp

    def find_by_id(self, id_bank):
        for bank in self.data:
            if bank['id'] == id_bank:
                id = Id(bank['id'])
                name = Name(bank['name'])
                logo = Logo(bank['logo'])
                abbreviation = Abbreviation(bank['abbreviation'])
                state = State(bank['state'])
                return Bank(id, name, logo, abbreviation, state)
