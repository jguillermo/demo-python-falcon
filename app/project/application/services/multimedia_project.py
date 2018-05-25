# -*- coding: utf-8 -*-

from project.domain.factories.entities.multimedia_project import MultimediaProjectFactory
from project.domain.factories.entities.multimedia import MultimediaFactory
from project.infrastructure.common.try_except import handler_except
from project.domain.valueObjects.multimedia import ALIAS_TYPE, IMAGE_TYPE, PANORAMIC_TYPE, LOGO_TYPE


class MultimediaProjectAppService:

    def __init__(self, domain_service, domain_multimedia, domain_images):
        self.__domain_service = domain_service
        self.__domain_multimedia = domain_multimedia
        self.__domain_images = domain_images

    @handler_except
    def find_by_id_project(self, id_project):
        result = []
        res = self.__domain_service.find_by_id_project(id_project)
        for multimediaProject, multimedias in res:
            data = MultimediaProjectFactory.get_multimedia_project(multimediaProject, multimedias)
            result.append(data)
        return result

    @handler_except
    def create(self, id_project, **kwargs):
        images = []
        for row in kwargs['multimedia']:
            if int(row['type']) in [IMAGE_TYPE, PANORAMIC_TYPE, LOGO_TYPE]:
                images.append({'name': row['name'], 'type': ALIAS_TYPE[int(row['type'])]})

            multimedia = MultimediaFactory.create(row)
            id_multimedia = self.__domain_multimedia.create(multimedia)

            multimedia_project = MultimediaProjectFactory.create(None, idMultimedia=id_multimedia, idProject=id_project)
            response = self.__domain_service.create(multimedia_project)

        self.__domain_images.create(images, id_project, kwargs['idUser'])

        return response
