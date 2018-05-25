# -*- coding: utf-8 -*-
from abc import ABC
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session


class SqlAlchemyAdapter(ABC):
    session = None
    entity = None

    def __init__(self, config):
        self._options = config.get_key('database')
        self._session_maker()

    def create(self, data):
        try:
            f = data
            self.session.add(f)
            self.session.commit()
            return f.id
        except Exception as e:
            self.session.rollback()
            raise e

    def update(self, id, **kwargs):
        try:
            result = self.find_by_id(id)
            for key, value in kwargs.items():
                setattr(result, key, value)
            return self.session.commit()
        except Exception as e:
            raise e

    def delete(self, id):
        try:
            result = self.find_by_id(id)
            self.session.delete(result)
            return self.session.commit()
        except Exception as e:
            raise e

    def find_all(self, params):
        select_params = params['fields']
        where_params = params['filter']
        pagination_params = params['pagination']
        sort_params = params['sort']

        query = self.session.query(self.entity)
        query = query.add_columns(*select_params)
        query = query.filter_by(**where_params)
        query = query.order_by(sort_params)
        if pagination_params:
            query = query.offset(pagination_params['offset']).limit(pagination_params['limit'])
        return query.all()

    def find_by_id(self, id):
        try:
            return self.session.query(self.entity).filter_by(id=id).first()
        except Exception as e:
            raise e

    def statement(self, sql):
        result = self.session.query(self.entity).from_statement(
            text(sql)
        )
        return result.all()

    def bulk_insert(self, list):
        try:
            return self.session.add_all(list)
        except Exception as e:
            raise e

    def delete_with_params(self, params):
        try:
            return self.session.query(self.entity).filter(params).delete(synchronize_session=False)
        except Exception as e:
            raise e

    def commit(self):
        try:
            return self.session.commit()
        except Exception as e:
            raise e

    def _session_maker(self):
        try:
            driver = '{}charset=utf8'.format(self._options['url'])
            engine = create_engine(driver, echo=True, isolation_level="READ UNCOMMITTED")
            self.session = scoped_session(sessionmaker(bind=engine))
        except Exception as e:
            raise e
