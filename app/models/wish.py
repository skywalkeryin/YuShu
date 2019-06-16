
# -*- coding: utf-8 -*-

'''
 Author :'skywalkeryin'
 Date :  2019-06-16
'''


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey(user.id))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
