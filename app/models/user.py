# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2019-06-05
'''

from sqlalchemy import Column, Integer, String,Boolean
from app.models.base import Base

class User(Base):
    id = Column(Integer, primary_key=True)
