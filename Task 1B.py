from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def change(x):
    result = []

    #Changes details of each station to list of tuples (station name, station town, distance)
    for tuple in x:
        result.append((tuple[0].name,tuple[0].town,tuple[1]))
    return result

def run():
    stations = build_station_list()
    stations_list = stations_by_distance(stations,(52.2053,0.1218))
    
    changed_list = change(stations_list)

    print(changed_list[:10])
    print("\n")
    print(changed_list[-10:])

if __name__ == "__main__":
    run()