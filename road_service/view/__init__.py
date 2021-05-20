from flask import Flask, Blueprint

from .base import IndexView


def set_up_view(app: Flask):
    mod = Blueprint('', __name__)

    mod.add_url_rule(
        '',
        view_func=IndexView.as_view('index')
    )

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/')
