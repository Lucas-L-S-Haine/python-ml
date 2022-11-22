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
