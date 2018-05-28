# -*- coding: utf-8 -*-

from evaluation.infrastructure.bus import CommandBusSync, QueryBusSync


class Base:

    def __init__(self) -> None:
        self.command_bus = CommandBusSync()
        self.command_query = QueryBusSync()

    def print(self,value):
        print('*****************************')
        print(value)
        print('--*************************--')
