import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list


#dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
#levels = [1,2,4,5,7,9,12,15,14,13,10,9,8,7,6,5,4,3]
#p = 6

#stations = build_station_list()
#station = stations[0]


#print(len(dates))
#print(len(levels))

def plot_water_level_with_fit(station, dates, levels, p):


    dates_x = matplotlib.dates.date2num(dates)
    poly = polyfit(dates_x, levels, p)
    poly_y = poly(dates_x)

    plt.plot(dates, levels, label='$Data$')
    plt.plot(dates, poly_y, label='$Poly$')
    plt.xlabel("$Time$")
    plt.ylabel("$Water Level$")
    plt.xticks(rotation=45);
    plt.legend()
    plt.show()
    return

#print(plot_water_level_with_fit(station, dates, levels, p))






#import matplotlib.pyplot as plt
#from datetime import datetime, timedelta

#def plot_water_levels(station, dates, levels):
#    plt.plot(dates,levels)

#    plt.xlabel('Date')
#    plt.ylabel('Water level (m)')
#    plt.xticks(rotation=45);
#    plt.title(station.name)

#    plt.tight_layout()

#    plt.show()