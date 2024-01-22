from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list
    stations_list = stations_by_distance(stations(52.2053,0.1218))
    
    print(stations_list[:10])
    print("\n")
    print(stations_list[-10:])

if __name__ == "__main__":
    run()