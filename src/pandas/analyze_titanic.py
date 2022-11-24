from load_titanic import titanic

# Read the first 8 entries
print(titanic.head(8))

# Convert data frame to Excel format
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
# Read from Excel spreadsheet
# table = pd.read_excel("titanic.xlsx", sheet_name="passengers")

# Read data types
print(titanic.dtypes)

# Print data summary
titanic.info()

# Take a particular series from the data frame.
# Column names available on titanic.columns
ages = titanic["Age"]
print(ages)

# Panda’s equivalent for R’s dim
print(titanic.shape)
print(titanic["Age"].shape)

# Select a subset of columns within the data frame
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())
