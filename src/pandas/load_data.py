import pandas as pd


# Store titanic data as a data frame
titanic = pd.read_csv("data/titanic.csv")
air_quality = pd.read_csv("data/air_quality_no2.csv",
                          index_col=0,
                          parse_dates=True)
