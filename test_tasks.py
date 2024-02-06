from floodsystem.geo import stations_by_distance
from haversine import haversine
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

stations = build_station_list()

#Check if distances are in order
def test_stations_by_distance():
    result = stations_by_distance(stations,p=(0,0))
    for i in range(1,len(result)):
        p = result[i]
        q = result[i-1]
        assert p[2] >= q[2]

#Check if all stations are within 10km
def test_stations_within_radius():
    coord = (52.2053, 0.1218)
    stations_list = stations_within_radius(stations,coord,10)
    for i in stations:
        for a in stations_list:
            if i.name == a:
                assert haversine(coord,i.coord) <= 10

#Check if stations have inconsistent data
def test_inconsistent_typical_range_stations():
    list = inconsistent_typical_range_stations(stations)
    for i in stations:
        for j in list:
            if i.name == j:
                assert  i.typicalrange[1] < i.typicalrange[0] or i.typicalrange == None 

#tests that each key in the dictionary stations_by_river is mapped to a tuple of station names
def test_stations_by_river(stations):
    test_stations_by_river = stations_by_river(stations)
    for river, stations_list in test_stations_by_river.items():
        assert isinstance(stations_list, tuple)


# tests that rivers_by_station_number returns a list of tuples containing a string and an integar
def test_rivers_by_station_number(stations):
    test_rivers_by_station_number = rivers_by_station_number(stations, 10)
    for tuple in test_rivers_by_station_number:
        river, number_of_stations = tuple
        assert isinstance(river, str)
        assert isinstance(number_of_stations, int)

