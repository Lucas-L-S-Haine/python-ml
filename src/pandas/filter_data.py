import pandas as pd


titanic = pd.read_csv("data/titanic.csv")


get_owen = lambda name: name.find("Owen") != -1
passenger_names = [passenger for passenger in filter(get_owen, titanic["Name"])]
passenger_data = [passenger for passenger in map(get_owen, titanic["Name"])]


print(passenger_names)
print(titanic[passenger_data])
