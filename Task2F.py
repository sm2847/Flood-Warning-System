import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list


stations = build_station_list()


def run():

        measure_id = station.measure_id
        dates, levels = fetch_measure_levels(measure_id, 2)
        plot_water_level_with_fit(station, dates, levels, 5)





if __name__ == "__main__":
    print("*** Task 2D: CUED Part IA Flood Warning System ***")
    run()

    

