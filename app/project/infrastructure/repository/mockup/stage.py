# -*- coding: utf-8 -*-

from project.domain.repository.stage import StageRepository
from project.domain.entities.stage import Stage
from project.domain.factories.entities.stage import StageFactory


class MockStageRepository(StageRepository):

    def __init__(self):
        self.data = [
            {'id': 1, 'name': 'En Pre-venta', 'alias': 'pre-venta', 'type': 1, 'state': 1},
            {'id': 2, 'name': 'En Construcción', 'alias': 'construccion', 'type': 1, 'state': 1}
        ]

    def create(self, stage: Stage):
        self.data.append(
            {'id': stage.id, 'name': stage.name, 'alias': stage.alias, 'type': stage.type, 'state': stage.state}
        )
        return True

    def update(self, stage):
        pass

    def delete(self, id):
        pass

    def find_all(self, params=None):
        resp = []
        for stage in self.data:
            resp.append(StageFactory.create(stage))
        return resp

    def find_by_id(self, id):
        for stage in self.data:
            if stage['id'] == id:
                return StageFactory.create(stage)
