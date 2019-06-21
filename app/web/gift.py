

from app.models.base import db
from . import web
from flask import  current_app, flash, redirect, url_for
from flask_login import login_required, current_user # It is a user instance
from app.models.gift import Gift

__author__ = 'skywalker'


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    Gift.get_wish_count(isbn_list)
    return 'My gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        #Transactions
        #rollback
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
    else:
        flash('This book is already in your gift list or wish list')
    return redirect(url_for('web.book_datail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



