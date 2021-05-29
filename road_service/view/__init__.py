from flask import Flask, Blueprint

from road_service.helpers.auth import is_login

from .base import IndexView
from .maps import MapsView
from .road import PitView


def set_up_view(app: Flask):
    mod = Blueprint('', __name__)

    mod.add_url_rule(
        '',
        view_func=IndexView.as_view('index')
    )

    mod.add_url_rule(
        'maps',
        view_func=MapsView.as_view('maps')
    )

    mod.add_url_rule(
        'pits',
        view_func=PitView.as_view('pits')
    )

    # mod.before_request(is_login)

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/')
