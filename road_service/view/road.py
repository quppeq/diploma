from flask import request, jsonify, g
from flask.views import MethodView

from road_service.db import db
from road_service.maps import maps

from road_service.models.road import Road


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
        lat = data['lat']
        lng = data['lng']

        x_acc = data.get('x_acc')
        y_acc = data.get('y_acc')
        z_acc = data.get('z_acc')

        road = Road(
            lat=lat,
            lng=lng,
            x_acc=x_acc,
            y_acc=y_acc,
            z_acc=z_acc,
        )
        db.session.add(road)
        db.session.commit()
        return jsonify({
            'lat': road.lat,
            'lng': road.lng
        })
