
# -*- coding: utf-8 -*-

'''
 Author :'skywalkeryin'
 Date :  2019-06-16
'''


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, desc,func

from app.models.base import Base, db
from sqlalchemy.orm import relationship


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        gifts = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)
        ).all()
        return gifts

    @classmethod
    def get_gifts_count(cls, isbn_list):
        # 根据传入的list， 到wish表中查询心愿的数量
        # db.session
        # 条件表达式 expression
        # mysql in
        from app.models.gift import Gift
        count_list = db.session.query(Wish.isbn, func.count(Gift.id)).filter(
            Gift.launched == False, Gift.isbn.in_(isbn_list), Gift.status == 1).group_by(
            Gift.isbn).all()
        # 返回对象 字典
        count_list = [{'isbn': count[0], 'count': count[1]} for count in count_list]
        return count_list

