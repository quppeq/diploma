from flask import render_template, redirect
from flask import current_app as app
from flask.views import MethodView
from flask_googlemaps import Map

from road_service.db import db
from road_service.maps import maps

from road_service.helpers.road_condition import scan_road


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
            ],
            style="height:600px;width:100%;margin:0;",
        )
        return render_template('map.jinja2', map=mymap)

    def post(self):
        multiple = app.config['MULTIPLE']
        scan_road(multiple)
        db.session.commit()
        return redirect('maps')

