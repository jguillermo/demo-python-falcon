# -*- coding: utf-8 -*-


class MultimediaImagesS3Repository:

    def __init__(self, s3_service):
        self.__s3_service = s3_service

    def create(self, images, id_project, id_user):
        try:
            self.__s3_service.copy_tmp_to_origin(images, id_project, id_user)
            self.__s3_service.copy_origin_to_redim(images, id_project, id_user)
        except Exception as e:
            raise e
