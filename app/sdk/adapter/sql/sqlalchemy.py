# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, text
from sqlalchemy.engine import ResultProxy
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session


class SqlAlchemySession:

    def __init__(self, config):
        self._options = config.get_key('database')

        self._session_maker()

    def _session_maker(self):
        try:
            driver = '{}?charset=utf8'.format(self._options['url'])
            engine = create_engine(driver, echo=True, isolation_level="READ UNCOMMITTED")
            self._session = scoped_session(sessionmaker(bind=engine))
        except Exception as e:
            raise e

    def getSession(self) -> Session:
        return self._session


class SqlAlchemyAdapter:
    _entity = None

    def __init__(self, sql_session: SqlAlchemySession):
        self.__session = sql_session.getSession()

    def persist(self, entity):
        try:
            self.__session.add(entity)
            self.__session.commit()
            return True
        except Exception as e:
            self.__session.rollback()
            raise e

    def find_by_id(self, id):
        return self.__session.query(self._entity).filter_by(id=id).first()


class SqlAlchemySearchAdapter:

    def __init__(self, sql_session: SqlAlchemySession):
        self.__session = sql_session.getSession()

    def query(self, sql_str: str) -> ResultProxy:

        sql = text(sql_str)
        return self.__session.execute(sql)

    def result(self, sql_str: str):
        result = self.query(sql_str)
        print(type(result))
        data = []
        for row in result:
            row_value = {}
            for value in row.keys():
                row_value[value] = row[value]
            data.append(row_value)
        return data
