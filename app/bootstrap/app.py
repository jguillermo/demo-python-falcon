# -*- coding: utf-8 -*-
from project.application.framework import FalconApi
from project.infrastructure.repository.sqlalchemy.mapping import load_mapper
from project.infrastructure.common.env import load_env_file


class App:
    def __init__(self):
        load_env_file('config/config.env')
        load_mapper()
        self.api = FalconApi().api
