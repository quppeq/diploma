import math
from road_service.db import db
from road_service.models.road import Road, Pit, RoadGroup
from road_service.models.user import User


def distance(lat1, lng1, lat2, lng2):
    degrees_to_radians = math.pi / 180.0

    phi1 = (90.0 - lat1) * degrees_to_radians
    phi2 = (90.0 - lat2) * degrees_to_radians

    theta1 = lng1 * degrees_to_radians
    theta2 = lng2 * degrees_to_radians


    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
           math.cos(phi1) * math.cos(phi2))
    arc = math.acos(cos)

    meter = arc * 6373 * 1000

    return meter


def scan_road(multiple):
    groups = db.session.query(RoadGroup).filter(
        RoadGroup.checked == False
    ).all()

    for group in groups:
        roads = group.roads
        prev = None
        for road in roads:
            if not prev:
                prev = road
                continue
            if road.z_acc > prev.z_acc * 2 + 1:
                db.session.add(Pit(
                    lat=road.lat,
                    lng=road.lng,
                    user_id=road.user_id,
                ))
    db.session.query()

