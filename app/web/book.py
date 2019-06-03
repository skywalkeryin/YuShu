from flask import request, jsonify, render_template

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection

import json

from . import web


class testObj:
    pass

@web.route('/test')
def test():

   r = {
       'name' : 'yin',
       'age' : 18
   }

   b = testObj()
   b.b = 3

   return  render_template('test.html', data = r, b = b)


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
            yushu_book.search_by_keyword(q)
            # result = BookViewModel.package_collection(result, q)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
    else:
        return jsonify(form.errors)
