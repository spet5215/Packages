# compute-mean.py
import numpy as np

import tstools
print(tstools.filename)

timeseries = np.genfromtxt("/Users/annagfairweather/pacakging/python-packaging-course/course/analysis1/data/brownian.csv", delimiter=",")

# instead of mean, var = tstools.moments.get_mean_and_var(...)
mean, var = tstools.get_mean_and_var(timeseries)

# instead of fig, ax = tstools.vis.plot_histogram(...)
fig, ax = tstools.plot_histogram(timeseries, nbins=100)