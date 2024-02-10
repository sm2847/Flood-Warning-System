from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    stations = build_station_list()
    
    update_water_levels(stations)

    stations = stations_level_over_threshold(stations,0.8)
    sorted_stations = sorted(stations, key=lambda tup:tup[1], reverse=True)

    for station in sorted_stations:
        print(station[0].name,station[1])

if __name__ == "__main__":
    run()
