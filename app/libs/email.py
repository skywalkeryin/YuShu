from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass
    pass


def send_mail(to, subject, template, **kwargs):
    #Python Email
    #
    msg = Message('[YUSHU]' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])

    msg.html = render_template(template, **kwargs)

    # Get the real flask app instance,  不是线程隔离的
    app = current_app._get_current_object()
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
