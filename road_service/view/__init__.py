from flask import Flask, Blueprint

from .base import IndexView
from .maps import MapsView

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

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/')
