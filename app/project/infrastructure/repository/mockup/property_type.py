# -*- coding: utf-8 -*-

from project.domain.repository.property_type import PropertyTypeRepository
from project.domain.entities.property_type import PropertyType
from project.domain.valueObjects.property_type import Id, Id_Parent, Name, Level, State


class MockPropertyTypeRepository(PropertyTypeRepository):

    def __init__(self):
        self.data = [
            {'id': 1, 'idParent': None, 'level': '1', 'name': 'Residencial', 'state': 1},
            {'id': 2, 'idParent': 1, 'level': 2, 'name': 'Departamentos', 'state': 1},
            {'id': 3, 'idParent': 2, 'level': 3, 'name': 'Departamento', 'state': 1},
            {'id': 4, 'idParent': 2, 'level': 3, 'name': 'Departamento Duplex', 'state': 1},
            {'id': 5, 'idParent': 2, 'level': 3, 'name': 'Departamento Triplex', 'state': 1},
            {'id': 6, 'idParent': 2, 'level': 3, 'name': 'Departamento de Playa', 'state': 1},
            {'id': 7, 'idParent': 2, 'level': 3, 'name': 'Departamento Loft', 'state': 1},
            {'id': 8, 'idParent': 2, 'level': 3, 'name': 'Departamento Penthouse', 'state': 1},
            {'id': 9, 'idParent': 1, 'level': 2, 'name': 'Casas', 'state': 1},
            {'id': 10, 'idParent': 9, 'level': 3, 'name': 'Casa', 'state': 1},
            {'id': 11, 'idParent': 9, 'level': 3, 'name': 'Casa de playa', 'state': 1},
            {'id': 12, 'idParent': 9, 'level': 3, 'name': 'Casa de playa en condominio', 'state': 1},
            {'id': 13, 'idParent': 9, 'level': 3, 'name': 'Casa de campo', 'state': 1},
            {'id': 14, 'idParent': 9, 'level': 3, 'name': 'Casa en condominio', 'state': 1},
            {'id': 15, 'idParent': None, 'level': 1, 'name': 'Comercial', 'state': 1},
            {'id': 16, 'idParent': 15, 'level': 2, 'name': 'Oficinas', 'state': 1},
            {'id': 17, 'idParent': 15, 'level': 2, 'name': 'Locales comerciales', 'state': 1},
            {'id': 18, 'idParent': None, 'level': 1, 'name': 'Lotes', 'state': 1},
            {'id': 19, 'idParent': 18, 'level': 2, 'name': 'Lotes / terrenos', 'state': 1}
        ]

    def create(self, property_type: PropertyType):
        self.data.append(
            {'id': property_type.id, 'name': property_type.name}
        )
        return True

    def update(self, property_type):
        pass

    def delete(self, id):
        pass

    def find_all(self, params=None):
        resp = []

        for property_type in self.data:
            id = Id(property_type['id'])
            id_parent = Id_Parent(property_type['idParent'])
            name = Name(property_type['name'])
            level = Level(property_type['level'])
            state = State(property_type['state'])
            resp.append(PropertyType(id, id_parent, name, level, state))
        return resp

    def find_by_id(self, id):
        for property_type in self.data:
            if property_type['id'] == id:
                id = Id(property_type['id'])
                id_parent = Id_Parent(property_type['idParent'])
                name = Name(property_type['name'])
                level = Level(property_type['level'])
                state = State(property_type['state'])
                return PropertyType(id, id_parent, name, level, state)
