from flask import request, jsonify, render_template, flash
from flask_login import current_user
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.Trade import TradeInfo
from app.view_models.book import BookViewModel, BookCollection

from . import web


@web.route('/book/search')
def search():
    """

    :param q: keyword or isbn
    :param page:   start or count
    :return:
    """
    form = SearchForm(request.args)
    books = BookCollection()
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        yushu_book = YuShuBook()
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
        else:
            yushu_book.search_by_keyword(q, page)
            # result = BookViewModel.package_collection(result, q)

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
    else:
        flash('Keyword is not correct. Please rekey in.')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):

    has_in_gifts = False
    has_in_wishes = False

    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True

        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book, gifts=trade_gifts_model, wishes=trade_wishes_model,
                           has_in_gifts = has_in_gifts, has_in_wishes=has_in_wishes)


