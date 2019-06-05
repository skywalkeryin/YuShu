# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2019-06-05
'''

from sqlalchemy import Column, Integer, String,Boolean
from app.models.base import Base

class Gift(Base):
    id = Column(Integer, primary_key=True)

    launched = Column(Boolean, default=False )