
from sqlalchemy import Column, Integer, String, SmallInteger


from app.models.base import Base


class Drift(Base):

    """
        一次具体的交易信息
    """
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)   #收件人
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))
    # 十一月

    # 赠送者信息
    donor_id = Column(Integer)
    gift_id = Column(Integer)
    donor_nickname = Column(String(20))

    pending = Column('pending', SmallInteger, default=1)