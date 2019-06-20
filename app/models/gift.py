# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2019-06-05
'''
from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc

from app.models.base import Base
from sqlalchemy.orm import relationship

from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    #对象代表一个礼物，具体
    #类代表礼物这一事物，它是抽象的， 不是具体的“一个”
    @classmethod
    def recent(self):

        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return  recent_gift

