from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    stations_list = stations_by_distance(stations,(52.2053,0.1218))
    
    closest_stations = stations_list[:10]
    furthest_stations = stations_list[-10:]

    for (station,distance) in closest_stations:
        print((station.name,station.town,distance))
    
    print("\n")
    
    for (station,distance) in furthest_stations:
        print((station.name,station.town,distance))

if __name__ == "__main__":
    run()