#!/usr/bin/env python3
from load_data import air_quality


# Data frame with 3 series
print(air_quality.head())

# Create another series from station_london
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

# Print resulting data frame. This one now has 4 series
print(air_quality.head())

# Create a ratio series from station_paris and station_antwerp
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)
print(air_quality.head())

# Create a new data frame with renamed series
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR4014",
        "station_london": "London Westminster"
    }
)
print(air_quality_renamed.head())

# Use mapping function to rename series
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed.head())
