from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt

def run():
    stations = build_station_list()
    update_water_levels(stations)

    station_levels = []
    for i in stations:
        if i.latest_level is None:
            continue
        else:
            station_levels.append(i.latest_level)

    station_levels.sort(reverse=True)

    max_levels = station_levels[0:5]

    max_5_stations = []

    for i in stations:
        for j in max_levels:
            if j == i.latest_level:
                max_5_stations.append(i)

    dt = 10
    



    for i in max_5_stations:
        dates,levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))

        typ_low = [i.typical_range[0]] * len(dates)
        typ_high = [i.typical_range[1]] * len(dates)
        plt.title("Station = " + i.name)
        plt.plot(dates, typ_low, label=("$Typical Low$"))
        plt.plot(dates, typ_high, label=("$Typical High$"))        
        plot_water_levels(i, dates, levels)

if __name__ == "__main__":
    run()