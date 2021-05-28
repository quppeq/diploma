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

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        )
    user = db.relationship('User', backref='roads')

    road_group_id = db.Column(db.Integer,
                              db.ForeignKey('road_group.id'),
                              )
    road_group = db.relationship('RoadGroup', backref='roads')

    date_creation = db.Column(db.DateTime, server_default=func.now())


class Pit(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        )
    user = db.relationship('User', backref='pits')

    date_creation = db.Column(db.DateTime, server_default=func.now())


class RoadGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        )
    user = db.relationship('User', backref='groups')

    checked = db.Column(db.Boolean,
                        nullable=False,
                        server_default='false',
                        )

    date_creation = db.Column(db.DateTime, server_default=func.now())
