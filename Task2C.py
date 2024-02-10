from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()
update_water_levels(stations)

def run():
    stations_list = stations_highest_rel_level(stations,10)

    for station in stations_list:
        print(station.name,station.relative_water_level())

if __name__ == "__main__":
    run()