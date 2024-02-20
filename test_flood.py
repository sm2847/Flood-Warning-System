from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.plot import plot_water_levels
import matplotlib.pyplot as plt
from Task2E import run as task2E_run
from floodsystem.analysis import polyfit
import numpy as np
from Task2G import run as task2G_run
from floodsystem.stationdata import build_station_list, update_water_levels

def test_stations():
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

    return [s1,s2,s3,s4,s5]

#Task 2B
def test_stations_level_over_thershold():

    stations = test_stations()

    stations[0].typical_range, stations[0].latest_level = (0, 5), 2.5
    stations[1].typical_range, stations[1].latest_level = (0, 2.5), 2.5 
    stations[2].typical_range, stations[2].latest_level = (0, 1), 0 

    over_threshold_stations = stations_level_over_threshold(stations, 0.2)

    assert over_threshold_stations[0][1] == 0.5
    assert over_threshold_stations[1][1] == 1

#Task 2C
def test_stations_highest_rel_level():
    
    stations = test_stations()
    
    stations[0].typical_range, stations[0].latest_level = (0.1, 0.5), 0.25
    stations[1].typical_range, stations[1].latest_level = (0.1, 1.5), 0.25
    stations[2].typical_range, stations[2].latest_level = (0.0, 2.5), 3.0
    stations[3].typical_range, stations[3].latest_level = (0.1, 0.5), 1.0
    stations[4].typical_range, stations[4].latest_level = (0.1, 2.5), 5.0
    [s1,s2,s3,s4,s5] = stations

    assert stations_highest_rel_level(stations, 1) == [s4]
    assert len(stations_highest_rel_level(stations, 5)) == 5
    assert stations_highest_rel_level(stations, 5) == [s4,s5,s3,s1,s2]


#Task 2E

def test_levels_graphing():
    
    task2E_run()
    num_figures = plt.gcf().number
    assert num_figures == 1




#Task 2F


def test_poly():
    test_data = [0, 1, 4, 9, 16, 25]
    test_xaxis = [0,1,2,3,4,5]

    test_polynomial = polyfit(test_xaxis, test_data, 2)
    for x in test_xaxis:
        poly_result = test_polynomial(x)
    expected_value = x ** 2
    assert np.isclose(poly_result, expected_value, atol=1e-8)


#Task 2G

def test_severity_rating():
    stations = build_station_list()
    update_water_levels(stations)
    
    num_of_stations = len(stations)        
    total = 0
    counter = 0
    
    list_severe_towns = []
    list_high_towns = []
    list_mod_towns = []
    list_low_towns = []

    for station in stations:
        if station.relative_water_level() != None:
            if station.relative_water_level() > 1.25:
                list_severe_towns.append(station.town)
            if 1 <= station.relative_water_level() < 1.25:
                list_high_towns.append(station.town)
            if 0.75 <= station.relative_water_level() < 1:
                list_mod_towns.append(station.town)
            if station.relative_water_level() < 0.75:
                list_low_towns.append(station.town)
        
        if station.relative_water_level() == None:
            counter += 1
            total +=1
    
    total += len(list_severe_towns) + len(list_high_towns) + len(list_mod_towns) + len(list_low_towns)

    assert total == num_of_stations-1
