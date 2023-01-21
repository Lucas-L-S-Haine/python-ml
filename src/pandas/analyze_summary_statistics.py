#!/usr/bin/env python
from load_data import titanic


# Calculate the arithmetic mean of age
print(titanic["Age"].mean(), end="\n\n")

# Calculate the median of two series
print(titanic[["Age", "Fare"]].median(), end="\n\n")

# Summarize the "Age" and "Fare" series
print(titanic[["Age", "Fare"]].describe(), end="\n\n")

# Use aggregating statistics
print(titanic.agg({"Age": ["min", "max", "median", "skew"],
                   "Fare": ["min", "max", "median", "mean"]}),
      end="\n\n")

# Group aggregating statistics by category
print(titanic[["Sex", "Age"]].groupby("Sex").mean(),
      end="\n\n")

# Take the mean of all numeric columns
print(titanic.groupby("Sex").mean(numeric_only=True),
      end="\n\n")

# Take a series out of grouped data and calculate the mean
print(titanic.groupby("Sex")["Age"].mean(),
      end="\n\n")
