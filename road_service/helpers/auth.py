import time
import jwt
import hashlib

from flask import request, g, abort
from flask import current_app as app

from road_service.db import db
from road_service.models.user import User

OPEN_API_ROUTES = ['login', 'registration', 'pits']


def hash_password(password) -> str:
    salt = app.config["SECRET_KEY"]
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()


def check_hash(password, hash) -> bool:
    return password == hash


def create_token(username: str, iat: int) -> str:
    headers = {"alg": "HS256", "typ": "JWT"}
    payload = {"iat": iat, "username": username}

    token = str(jwt.encode(payload, app.config['SECRET_KEY'], headers=headers), "utf-8")
    return token


def decode_token(token: str):
    try:
        decoded_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
        return decoded_token
    except:
        return None


def auth():
    if '/static/' in request.path:
        return
    token = request.headers.get('Authorization')
    user = None
    if token:
        data = decode_token(token)
        if int(data['iat']) + int(app.config.get('TIME_TO_LIVE', 3600 * 24 * 30)) > time.time():
            username = data['username']
            user = db.session.query(User).filter(User.username == username).first()
    g.user = user


def is_login():
    if (not g.user) and request.endpoint not in OPEN_API_ROUTES:
        abort(401)
