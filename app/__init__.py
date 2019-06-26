

from flask import Flask

from app.models.base import db
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate


login_manager = LoginManager()
mail = Mail()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = 'Please register or login'

    mail.init_app(app)

    from app.models.base import Base
    from app.models.book import Book
    db.init_app(app)
    # Migrate
    migrate.init_app(app, db=db)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web import web

    app.register_blueprint(web)

