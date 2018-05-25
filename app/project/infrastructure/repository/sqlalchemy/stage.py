# -*- coding: utf-8 -*-

from project.domain.repository.stage import StageRepository
from project.domain.entities.stage import Stage


class StageSqlAlchemyRepository(StageRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = Stage

    def create(self, stage: Stage):
        try:
            stageid = self.__adapter.create(stage)
            return {'idStage': stageid}
        except Exception as e:
            raise e

    def update(self, stage: Stage):
        try:
            kwargs = {'name': stage.name}
            return self.__adapter.update(stage.id, **kwargs)
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            return self.__adapter.delete(id)
        except Exception as e:
            raise e

    def find_all(self, params):
        try:
            return self.__adapter.find_all(params)
        except Exception as e:
            raise e

    def find_by_id(self, id):
        try:
            return self.__adapter.find_by_id(id)
        except Exception as e:
            raise e
