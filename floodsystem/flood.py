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