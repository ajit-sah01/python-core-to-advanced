from script.load import load_data
from script.clean import clean_data
from script.analyze import analyze_data

# Step 1: Load
df = load_data("data/data.csv")

# Step 2: Clean
df = clean_data(df)

# Step 3: Analyze
result = analyze_data(df)
print(result)
