#!/usr/bin/env python3
from load_data import titanic, air_quality


# Sort data by age
sorted_data = titanic.sort_values(by="Age")
print(sorted_data[["Name", "Age"]].head(8))

# Sort by cabin class and age in descending order
sorted_data = titanic.sort_values(by=['Pclass', 'Age'], ascending=False)
print(sorted_data[["Name", "Age", "Pclass"]].head(8))
