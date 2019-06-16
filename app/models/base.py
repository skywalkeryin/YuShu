# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2019-06-05
'''
from contextlib import contextmanager
from sqlalchemy import Column, SmallInteger, Integer
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy



class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)



