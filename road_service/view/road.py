from flask import request, jsonify, g
from flask.views import MethodView

from road_service.db import db
from road_service.maps import maps

from road_service.models.road import Road


class RoadView(MethodView):

    def get(self):
        roads = db.session.query(Road).filter(
            Road
        ).all()
        return jsonify(
            {
                'lat': road.lat,
                'lng': road.lng
            }
            for road in roads
        )

    def post(self):
        data = request.json
        lat = data['lat']
        lng = data['lng']

        road = Road(
            lat=lat,
            lng=lng,
        )
