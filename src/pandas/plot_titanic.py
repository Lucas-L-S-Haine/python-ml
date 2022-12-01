from load_data import air_quality
import matplotlib.pyplot as plt


print(air_quality.head())


# Plot data as a time series
air_quality.plot()
plt.show()
