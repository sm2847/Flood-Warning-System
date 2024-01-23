# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations,p):
    #Given list of stations and a point p it should return a list of station, distance tuples
    result = []

    for station in stations:
        coord = station.coord
        distance = haversine(coord,p)

        result.append((station,distance))
    return sorted_by_key(result,1)

def stations_within_radius(stations, centre, r):
    stations_inside = []
    sorted_stations_inside = []

    for station in stations:
        distance = haversine(station.coord,centre)
        if distance <= r:
            stations_inside.append(station.name) 
    
    sorted_stations_inside = sorted(stations_inside)

    return sorted_stations_inside