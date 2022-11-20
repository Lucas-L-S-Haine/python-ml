import pandas as pd

# Store titanic data as a data frame
titanic = pd.read_csv("data/titanic.csv")

# Read the first 8 entries
print(titanic.head(8))
