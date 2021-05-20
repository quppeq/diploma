from road_service.db import db


class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # geo data
