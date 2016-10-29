#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.signin'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Register all the filter.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app