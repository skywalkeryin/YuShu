
from . import web
from flask_login import login_required

__author__ = 'skywalker'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My gifts'


@web.route('/gifts/book/<isbn>')
def save_to_gifts(isbn):
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



