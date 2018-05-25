# -*- coding: utf-8 -*-


class MultimediaImagesDomainService(object):

    def __init__(self, repository):
        self.repository = repository

    def create(self, images, id_project, id_user):
        try:
            self.repository.create(images, id_project, id_user)
        except Exception as e:
            raise e
