# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2019-06-05
'''


from sqlalchemy import Column, SmallInteger, Integer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)



