from flask import current_app as app
from flask import request, jsonify, g
from flask.views import MethodView

from road_service.db import db

from road_service.models.road import Road, RoadGroup


class RoadView(MethodView):

    def get(self):
        roads = db.session.query(Road).filter(
        ).all()
        return jsonify(
            [{
                'lat': road.lat,
                'lng': road.lng
            }
                for road in roads]
        )

    def post(self):
        data = request.json
        roads = data['roads']
        road_group = RoadGroup(user_id=g.user.id)
        db.session.add(road_group)
        db.session.flush()
        for road in roads:
            lat = road['lat']
            lng = road['lng']

            x_acc = road.get('x_acc')
            y_acc = road.get('y_acc')
            z_acc = road.get('z_acc')

            road = Road(
                lat=lat,
                lng=lng,
                x_acc=x_acc,
                y_acc=y_acc,
                z_acc=z_acc,
                road_group_id=road_group.id,
                user_id=g.user.id
            )
            db.session.add(road)
        db.session.commit()
        return jsonify({
            'status': 'ok!'
        })
