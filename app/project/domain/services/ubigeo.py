# -*- coding: utf-8 -*-


class UbigeoDomainService(object):

    def __init__(self, department_repository, province_repository, district_repository, user_repository):
        self.department_repository = department_repository
        self.province_repository = province_repository
        self.district_repository = district_repository
        self.user_repository = user_repository

    def find_department_by_id(self, id):
        try:
            resp = self.department_repository.find_by_id(id)
            return resp
        except Exception as e:
            raise e

    def find_province_by_id(self, id):
        try:
            resp = self.province_repository.find_by_id(id)
            return resp
        except Exception as e:
            raise e

    def find_district_by_id(self, id):
        try:
            resp = self.district_repository.find_by_id(id)
            return resp
        except Exception as e:
            raise e

    def find_profile_by_id(self, id):
        try:
            resp = self.user_repository.find_by_id(id)
            return resp
        except Exception as e:
            raise e
