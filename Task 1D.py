from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


stations = build_station_list()
stationlist = sorted(rivers_with_station(stations))

print(len(stationlist))

first_ten = [0]*10
for i in range(10):
    first_ten[i] = stationlist[i]

print(first_ten)


river_stations_dict = stations_by_river(stations)

aire = sorted(river_stations_dict['River Aire'])
cam = sorted(river_stations_dict['River Cam'])
thames = sorted(river_stations_dict['River Thames'])

print(aire)
print(cam)
print(thames)

print(stations_by_river(stations))