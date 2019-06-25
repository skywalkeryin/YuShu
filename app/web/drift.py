

from app.models.gift import Gift
from . import web
from flask_login import login_required, current_user
from flask import flash, redirect, url_for, render_template

__author__ = 'skywalkeryin'


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
@login_required
def send_drift(gid):
    current_gift = Gift.query.get_or_404(gid)

    if current_gift.is_yourself_gift(current_user.id):
        flash('This book belong to you already, you can not ask yourself for this book.')
        return redirect(url_for('web.book_detail', isbn=current_gift.isbn))

    can = current_user.can_send_gift

    if not can:
        return render_template('not_enough_beans.html', beans=current_user.beans)

    donor = current_gift.user.summary
    return render_template('drift.html', donor=donor)



@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass
