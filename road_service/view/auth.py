import time
import logging
from flask import current_app as app
from flask import jsonify, request
from flask.views import MethodView

from road_service.db import db

from road_service.models.user import User

from road_service.helpers.auth import (
    hash_password,
    check_hash,
    create_token
)

logger = logging.getLogger(__name__)


class Login(MethodView):

    def post(self):
        data: dict = request.json
        username = data['username']
        password = data['password']

        user = db.session.query(User).filter(
            User.username == username
        ).first()
        u_password = user.password
        if not app.config['DEBUG']:
            hashed = hash_password(password)
            if not check_hash(u_password, hashed):
                return jsonify(dict(err='Неверный логин или пароль')), 401
        token = create_token(username, int(time.time()))
        logger.info(f"Successful login {username}")

        return jsonify(dict(authUser={'isSuccess': True,
                                      'token': token,
                                      'firstName': user.first_name,
                                      'lastName': user.last_name,
                                      'username': user.username,
                                      }))


class Registration(MethodView):

    def post(self):
        data: dict = request.json
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        password = data['password']

        hashed = hash_password(password)

        check = db.session.query(User).filter(
            User.username == username
        ).first()
        if check:
            return jsonify({"err": "Username is created"}), 400
        user = User(
            username=username,
            password=hashed,
            first_name=first_name,
            last_name=last_name
        )
        db.session.add(user)
        db.session.commit()

        return jsonify({
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
        })

