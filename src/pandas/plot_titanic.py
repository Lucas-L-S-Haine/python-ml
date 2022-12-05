from load_data import air_quality
import matplotlib.pyplot as plt


print(air_quality.head())


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
