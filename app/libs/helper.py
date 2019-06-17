# -*- coding: utf-8 -*-
from urllib.parse import urlparse, urljoin
from flask import request, url_for

__author__ = "skywalkeryin"


def is_isbn_or_key(q):
    """

    :param q: search value from the frontend
    :return:
    """
    # isbn isbn 13 digits
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key


def is_safe_url(next):
    if  not next:
        return False
    #next not null
    if  not next.startswith('/'):
        ref_url = urlparse(request.host_url)
        test_url = urlparse(next)
        return next and test_url.scheme in ('http', 'https') and \
               ref_url.netloc == test_url.netloc
    else:
        return True
