#!/usr/bin/env python
from load_data import titanic


# Calculate the arithmetic mean of age
print(titanic["Age"].mean(), end="\n\n")

# Calculate the median of two series
print(titanic[["Age", "Fare"]].median(), end="\n\n")
