import pandas as pd

# Store titanic data as a data frame
titanic = pd.read_csv("data/titanic.csv")

# Read the first 8 entries
print(titanic.head(8))

# Convert data frame to Excel format
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
