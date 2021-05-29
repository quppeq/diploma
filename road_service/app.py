import os
import logging
from flask import Flask

from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server

from road_service.db import db
from road_service.maps import maps
from road_service.config import configure_app, load_secrets

from road_service.helpers.auth import auth

from road_service.view import set_up_view

log = logging.getLogger(__name__)

ROOT_FOLDER = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_FOLDER = os.path.join(ROOT_FOLDER, 'templates')
STATIC_FOLDER = os.path.join(ROOT_FOLDER, 'static')


def configure_db(app: Flask):
    db.init_app(app)
    Migrate(app, db)


def configure_maps(app: Flask):
    maps.init_app(app)


def configure_manager(app: Flask) -> Manager:
    manager = Manager(app)
    manager.add_command("runserver", Server(host='0.0.0.0', threaded=True))
    manager.add_command('db', MigrateCommand)
    return manager


def create_app():
    app = Flask(
        __name__,
        template_folder=TEMPLATE_FOLDER,
        static_folder=STATIC_FOLDER,
    )
    configure_app(app)
    app.config.update(load_secrets(app.config['BASE_DIR']))
    app.debug = os.getenv("DEBUG", True)

    configure_db(app)
    configure_maps(app)

    app.before_request(auth)
    set_up_view(app)

    app.manager = configure_manager(app)

    return app
