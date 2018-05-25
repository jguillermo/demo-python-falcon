# -*- coding: utf-8 -*-

from project.domain.entities.project import Project
from project.infrastructure.common.try_except import handler_except


class HomeAppService(object):

    limit = 4

    def __init__(self, domain_service, domain_ubigeo):
        self.__domain_service = domain_service
        self.__domain_service_ubigeo = domain_ubigeo

    @handler_except
    def highlight(self):
        project_list = self.__domain_service.shuffle()

        if len(project_list) < self.limit:
            project_list = []

        result = []
        for project in project_list[0:self.limit]:
            fields = [attr for attr in project.__dict__.keys() if not attr.startswith('_')]
            ubigeo = self.__get_ubigeo(project)
            user = self.__get_profile(project)
            row = {}
            for field in fields:
                if field.startswith('date'):
                    row.update({field: getattr(project, field).strftime('%d/%m/%Y')})
                else:
                    row.update({field: getattr(project, field)})
                row.update({'ubigeo': ubigeo})
                row.update({'user': user})
            result.append(row)
        return result

    def __get_ubigeo(self, project: Project):
        ubigeo = dict()
        department = self.__domain_service_ubigeo.find_department_by_id(project.idDepartment)
        ubigeo['department'] = department.dict
        province = self.__domain_service_ubigeo.find_province_by_id(project.idProvince)
        ubigeo['province'] = province.dict
        district = self.__domain_service_ubigeo.find_district_by_id(project.idDistrict)
        ubigeo['district'] = district.dict
        return ubigeo

    def __get_profile(self, project: Project):
        profile_dict = dict()
        profile = self.__domain_service_ubigeo.find_profile_by_id(project.idProfile).dict
        profile_dict['idUser'] = profile['userId'] if profile else None

        return profile_dict
