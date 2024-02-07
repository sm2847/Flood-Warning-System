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


def rivers_with_station(stations):
    # returns a list of all the unique river names
    river_names = set()

    for station in stations:
        river_names.add(station.river)

    return river_names


def stations_by_river(stations):
    # returns a dictionary of all the stations that are on each river
    stations_on_river = {}
    for station in stations:
        if station.river in stations_on_river:
            stations_on_river[station.river] += (station.name,)
        else:
            stations_on_river[station.river] = station.name,
    
    return stations_on_river


def rivers_by_station_number(stations, N):
    # returns a lists of tuples containing rivers with the number of stations on them, in descending order
    stat_by_river_output = stations_by_river(stations)
    riv_stat_num = [(river, len(stat_by_river_output[river])) for river in stat_by_river_output]
    
    sorted_riv_stat_num = sorted(riv_stat_num, key=lambda x: x[1], reverse=True)
    N_sorted_riv_stat_num = sorted_riv_stat_num[:N]
    return N_sorted_riv_stat_num
    
