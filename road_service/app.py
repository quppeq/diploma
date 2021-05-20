import os
from flask import Flask

from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from road_service.db import db
from road_service.config import secrets


def configure_db(app: Flask):
    db.init_app(app)


def configure_manager(app: Flask) -> Manager:
    manager = Manager(app)
    manager.add_command("runserver", Server(host='0.0.0.0', threaded=True))
    manager.add_command('db', MigrateCommand)
    return manager


def create_app():
    app = Flask(__name__)
    app.config.update(secrets)
    app.debug = os.getenv("DEBUG", True)

    configure_db(app)
    app.manager = configure_manager(app)

    return app
