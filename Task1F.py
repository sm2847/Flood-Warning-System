from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    result = inconsistent_typical_range_stations(stations)

    result = sorted(station.name for station in result)

    print(result)

if __name__ == "__main__":
    run()
