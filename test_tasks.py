from floodsystem.geo import stations_by_distance
from haversine import haversine
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.station import MonitoringStation 

#Checks Task 1B function
def test_distance():
    stations = build_station_list()
    coord = (52.2053,0.1218)
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "test station"
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations.append(s)
    sorted = stations_by_distance(stations,coord)
    assert sorted[0][0]==s #Checks whether closest station is test station

#Check if all stations are within 10km
def test_stations_within_radius():
    stations = build_station_list()
    coord = (52.2053, 0.1218)
    stations_list = stations_within_radius(stations,coord,10)
    for i in stations:
        for a in stations_list:
            if i.name == a:
                assert haversine(coord,i.coord) <= 10

#Check if stations have inconsistent data
def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    list = inconsistent_typical_range_stations(stations)
    for i in stations:
        for j in list:
            if i.name == j:
                assert  i.typicalrange[1] < i.typicalrange[0] or i.typicalrange == None 

#tests that each key in the dictionary stations_by_river is mapped to a tuple of station names
def test_stations_by_river():
    stations = build_station_list()
    test_stations_by_river = stations_by_river(stations)
    for river, stations_list in test_stations_by_river.items():
        assert isinstance(stations_list, tuple)

# tests that rivers_by_station_number returns a list of tuples containing a string and an integar
def test_rivers_by_station_number():
    stations = build_station_list()
    test_rivers_by_station_number = rivers_by_station_number(stations, 10)
    for tuple in test_rivers_by_station_number:
        river, number_of_stations = tuple
        assert isinstance(river, str)
        assert isinstance(number_of_stations, int)

