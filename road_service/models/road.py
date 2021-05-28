from sqlalchemy import func

from road_service.db import db


class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # geo data
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    x_acc = db.Column(db.Float)
    y_acc = db.Column(db.Float)
    z_acc = db.Column(db.Float)

    date_creation = db.Column(db.DateTime, server_default=func.now())


class Pit(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    date_creation = db.Column(db.DateTime, server_default=func.now())
