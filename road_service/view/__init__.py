from flask import Flask, Blueprint

from .base import IndexView
from .maps import MapsView
from .road import RoadView
from .user import UserView


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
        'road',
        view_func=RoadView.as_view('road')
    )

    mod.add_url_rule(
        'user',
        view_func=UserView.as_view('user')
    )

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/')
