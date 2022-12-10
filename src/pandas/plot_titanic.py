#!/usr/bin/env python
import os

from load_data import air_quality
import matplotlib.pyplot as plt


# Plot data as a time series
air_quality.plot()
plt.show()

# Plot a single series out of the data frame
air_quality["station_paris"].plot()
plt.show()

# Create a scatter plot to compare London and Paris
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

# Create a boxplot for each available series
air_quality.plot.box()
plt.show()

# Plot each series separately
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()

# Extend, customize and save plot
if not os.path.exists("output"):
    os.mkdir("output")
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("output/no2_concentration.png")
plt.show()
