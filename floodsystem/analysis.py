import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def polyfit(dates, levels, p):
    dates_x = matplotlib.dates.date2num(dates)
    poly_coeff = np.polyfit(dates, levels, p)
    poly = np.poly1d(poly_coeff)
    return poly

