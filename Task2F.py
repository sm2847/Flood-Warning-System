import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels
from plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level


stations = build_station_list()
#top_five_risks =

data = stations_highest_rel_level(stations, 5)

















#print(stations_highest_rel_level(stations, 0))

#def run():
#        for station, rel_level in top_five_risks:
#                measure_id = station.measure_id
#                dates, levels = fetch_measure_levels(measure_id, 2)
#                plot_water_level_with_fit(station, dates, levels, 5)
#        plt.show()
#        return


#print(top_five_risks)


#if __name__ == "__main__":
#    print("*** Task 2D: CUED Part IA Flood Warning System ***")
#    run()
