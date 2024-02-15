from floodsystem.station import MonitoringStation
from floodsystem.station import consistent_typical_range_stations
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    
    stations = consistent_typical_range_stations(stations)
    list_level_over_threshold = []

    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                list_level_over_threshold.append((station, station.relative_water_level()))
    
    return list_level_over_threshold 

def stations_highest_rel_level(stations, N):
    
    list_stations_relative_levels = []

    for station in stations:
        if station.relative_water_level() is not None:
            list_stations_relative_levels.append((station, station.name, station.relative_water_level()))
    list_stations_relative_levels = sorted_by_key(list_stations_relative_levels, 2)
    stations_with_highest_relative_levels = []
    index = -1
    for i in range(N):
        stations_with_highest_relative_levels.append(list_stations_relative_levels[index][0])
        index -= 1
    return stations_with_highest_relative_levels