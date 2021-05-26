from road_service.db import db


class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # geo data
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
