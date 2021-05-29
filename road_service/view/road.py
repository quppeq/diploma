from flask import current_app as app
from flask import request, jsonify, render_template, g, redirect
from flask.views import MethodView
from flask_googlemaps import Map

from road_service.db import db
from road_service.maps import maps

from road_service.models.road import Road, Pit, RoadGroup

from road_service.helpers.road_condition import scan_road


class PitView(MethodView):

    def get(self):
        pits = db.session.query(Pit).all()

        markers = [{
            'lat': pit.lat,
            'lng': pit.lng,
            'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
            'infobox': "<b>Яма користувача {}</b>".format(pit.user.username),
        } for pit in pits]
        lat = markers[0]['lat'] if markers else 0
        lng = markers[0]['lng'] if markers else 0

        mymap = Map(
            identifier="map",
            lat=lat,
            lng=lng,
            markers=markers,
            style="height:600px;width:100%;margin:0;",
        )
        return render_template('map.jinja2', map=mymap)


    def post(self):
        multiple = app.config['MULTIPLE']
        scan_road(multiple)
        db.session.commit()
        return redirect('pits')

