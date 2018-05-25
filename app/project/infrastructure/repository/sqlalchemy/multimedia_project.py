# -*- coding: utf-8 -*-
from project.domain.repository.multimedia_project import MultimediaProjectRepository
from project.domain.entities.multimedia_project import MultimediaProject
from project.domain.entities.multimedia import Multimedia


class MultimediaProjectSqlAlchemyRepository(MultimediaProjectRepository):

    def __init__(self, adapter):
        self.__adapter = adapter
        self.__adapter.entity = MultimediaProject

    def create(self, multimedia_project: MultimediaProject):
        try:
            return self.__adapter.create(multimedia_project)
        except Exception as e:
            raise e

    def find_by_id_project(self, id_project):
        try:
            return self.__adapter.session.query(MultimediaProject, Multimedia).join(Multimedia, Multimedia.id == MultimediaProject.idMultimedia). \
                filter(MultimediaProject.idProject == id_project).all()
        except Exception as e:
            raise e
