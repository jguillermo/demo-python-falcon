# -*- coding: utf-8 -*-

from project.domain.entities.multimedia_project import MultimediaProject
from project.domain.entities.multimedia import Multimedia
from project.domain.valueObjects.multimedia_project import Id, IdProject, IdMultimedia


class MultimediaProjectFactory:

    @staticmethod
    def create(id=None, **kwargs):
        id = Id(kwargs['id'] if 'id' in kwargs else id)
        id_multimedia = IdMultimedia(kwargs['idMultimedia'])
        id_project = IdProject(kwargs['idProject'])

        multimedia_project = MultimediaProject(id.value, id_multimedia.value, id_project.value)
        multimedia_project.to_dict(kwargs)
        return multimedia_project

    @staticmethod
    def get_multimedia_project(multimedia_project: MultimediaProject, multimedia: Multimedia):
        return {
            'idProject': multimedia_project.idProject,
            'idService': multimedia_project.idMultimedia,
            'nombre': multimedia.name,
            'type': multimedia.type
        }
