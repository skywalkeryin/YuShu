# -*- coding: utf-8 -*-


'''
 Author :'skywalkeryin'
 Date :  2019-06-05
'''
from flask import current_app
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc, func

from app.models.base import Base, db
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

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)
        ).all()
        return gifts

    @classmethod
    def get_wish_count(cls, isbn_list):
        # 根据传入的list， 到wish表中查询心愿的数量
        # db.session
        # 条件表达式 expression
        # mysql in
        count_list = db.session.query(Wish.isbn, func.count(Wish.id)).filter(
            Wish.launched == False, Wish.isbn.in_(isbn_list), Wish.status == 1).group_by(
            Wish.isbn).all()
        # 返回对象 字典
        count_list = [{'isbn': count[0], 'count': count[1]} for count in count_list]
        return count_list


    #对象代表一个礼物，具体
    #类代表礼物这一事物，它是抽象的， 不是具体的“一个”
    @classmethod
    def recent(cls):

        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return  recent_gift


from app.models.wish import Wish