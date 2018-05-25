# -*- coding: utf-8 -*-
from abc import ABC
import requests


class ServicesAdapter(ABC):
    session = None
    entity = None
    name_microservice = None
    name_resource = None

    def __init__(self, config):
        self.__config_service = config.get_key('services')

    def find_by_id(self, id):
        try:
            return self.entity.create(self._get_data_request(id))
        except Exception as e:
            raise e

    def find_all(self):
        try:
            result = []
            response_list = self._get_data_request()
            for row_list in response_list:
                row = self.entity.create(row_list)
                result.append(row)
            return result
        except Exception as e:
            raise e

    def _get_data_request(self, id = None):
        try:
            if id is None:
                url = self.__get_url()
            else:
                url = self.__get_url().replace('{id}', str(id))

            response = requests.get(url)
            response_json = response.json()
            return response_json['data'][0] if response_json['data'] else response_json['data']
        except Exception as e:
            return {}

    def __get_url(self):
        try:
            config_service = self.__config_service
            host = config_service['host_base']
            prefix = config_service['rest'][self.name_microservice]['prefix']
            resources = config_service['rest'][self.name_microservice]['resource']
            url = host + prefix + resources[self.name_resource]
            return url
        except Exception as e:
            raise e
