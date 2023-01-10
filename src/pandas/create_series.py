#!/usr/bin/env python
from load_data import air_quality


# Data frame with 3 series
print(air_quality.head())

# Create another series from station_london
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

# Print resulting data frame. This one now has 4 series
print(air_quality.head())
