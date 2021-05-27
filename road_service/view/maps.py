from flask import render_template
from flask.views import MethodView
from flask_googlemaps import Map

from road_service.db import db
from road_service.maps import maps


class MapsView(MethodView):

    def get(self):
        mymap = Map(
            identifier="map",
            lat=50.4419,
            lng=35.1419,
            markers=[
                {
                    'lat': 50.4419,
                    'lng': 35.1419,
                    'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
                    'infobox': "<b>Яма!</b>"
                },
            ]
        )
        return render_template('map.jinja2', map=mymap)
