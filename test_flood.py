from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold


#Generates list of test stations

def generate_test_station():

    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["Station 1", "Station 2", "Station 3", "Station 4", "Station 5"]
    coord = [(0, 4), (0, 8), (0, 12), (0, 16), (0, 20)]
    trange = (-2.3, 3.4445)
    river = ("River X", "River Y", "River Z")
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label[0], coord[0], trange, river[0], town)
    s2 = MonitoringStation(s_id, m_id, label[1], coord[1], trange, river[1], town)
    s3 = MonitoringStation(s_id, m_id, label[2], coord[2], trange, river[0], town)
    s4 = MonitoringStation(s_id, m_id, label[3], coord[3], trange, river[1], town)
    s5 = MonitoringStation(s_id, m_id, label[4], coord[4], trange, river[2], town)

    return [s1, s2, s3, s4, s5]

#Task 2B
def test_stations_level_over_thershold():
    stations = generate_test_station()
    stations[0].typical_range, stations[0].latest_level = (0, 5), 2.5
    stations[1].typical_range, stations[1].latest_level = (0, 2.5), 2.5 
    stations[2].typical_range, stations[2].latest_level = (0, 1), 0 

    over_threshold_stations = stations_level_over_threshold(stations, 0.2)

    assert over_threshold_stations[0][1] == 0.5
    assert over_threshold_stations[1][1] == 1

#Task 2C
def test_stations_highest_rel_level():
    stations = generate_test_station()
    stations[0].typical_range, stations[0].latest_level = (0.1, 0.5), 0.25
    stations[1].typical_range, stations[1].latest_level = (0.1, 1.5), 0.25
    stations[2].typical_range, stations[2].latest_level = (0.0, 2.5), 3.0
    stations[3].typical_range, stations[3].latest_level = (0.1, 0.5), 1.0
    stations[4].typical_range, stations[4].latest_level = (0.1, 2.5), 5.0
    [s1,s2,s3,s4,s5] = stations

    assert stations_highest_rel_level(stations, 1) == [s4]
    assert len(stations_highest_rel_level(stations, 5)) == 5
    assert stations_highest_rel_level(stations, 5) == [s4,s5,s3,s1,s2]