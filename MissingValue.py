import pandas as pd
import numpy as np

# Create sample data with missing values
data = {
    "Name": ["A", "B", "C", "D"],
    "Marks": [85, np.nan, 90, np.nan]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull())

# Fill missing values with mean
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter Handling Missing Values:")
print(df)