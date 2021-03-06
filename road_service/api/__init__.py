from flask import Flask, Blueprint

from road_service.helpers.auth import is_login

from .road import RoadView
from .user import UserView
from .auth import Login, Registration


def set_up_api(app: Flask):
    mod = Blueprint('api', __name__)

    mod.add_url_rule(
        'road',
        view_func=RoadView.as_view('road')
    )


    mod.add_url_rule(
        'user',
        view_func=UserView.as_view('user')
    )

    mod.add_url_rule(
        'login',
        view_func=Login.as_view('login')
    )

    mod.add_url_rule(
        'registration',
        view_func=Registration.as_view('registration')
    )

    mod.before_request(is_login)

    # Реєстрація блюпрінта
    app.register_blueprint(mod, url_prefix='/api')
