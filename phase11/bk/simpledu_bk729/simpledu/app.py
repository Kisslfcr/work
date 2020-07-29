from flask import Flask, render_template
from flask_migrate import Migrate

from simpledu.config import configs
from simpledu.models import db, whooshee, Course, User
from flask_login import LoginManager

def register_extensions(app):
    db.init_app(app)
    Migrate(app, db)
    whooshee.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'

def register_blueprints(app):
    from .handlers import front, course, admin
    for bp in [front,course,admin]:
        app.register_blueprint(bp)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    register_extensions(app)
    register_blueprints(app)
    return app
