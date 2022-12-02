from load_data import air_quality
import matplotlib.pyplot as plt


print(air_quality.head())


# Plot data as a time series
air_quality.plot()
plt.show()

# Plot a single series out of the data frame
air_quality["station_paris"].plot()
plt.show()
