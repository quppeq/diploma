from flask import request, jsonify, g
from flask.views import MethodView

from road_service.db import db

from road_service.models.user import User


class UserView(MethodView):

    def get(self):
        data = request.json
        user_id = data['user_id']
        user = db.session.query(User).filter(
            User.id == user_id
        ).first()
        if not user:
            return jsonify({'err': 'bad user_id!'}), 400
        return jsonify(dict(
            username=user.username
        ))
