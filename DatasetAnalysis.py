import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("clv_data.csv")

# take first 30 rows
df = df.head(30)

print("Dataset Loaded Successfully!\n")

# ================== 1. BAR CHART ==================
data_bar = df.groupby("city")["purchases"].sum()

plt.figure()
data_bar.plot(kind='bar')
plt.xlabel("City")
plt.ylabel("Total Purchases")
plt.title("Bar Chart: Purchases by City")
plt.show()

# ================== 2. LINE CHART ==================
plt.figure()
plt.plot(df["days_on_platform"], df["purchases"], marker='o')
plt.xlabel("Days on Platform")
plt.ylabel("Purchases")
plt.title("Line Chart")
plt.show()

# ================== 3. PIE CHART ==================
plt.figure()
plt.pie(data_bar, labels=data_bar.index, autopct='%1.1f%%')
plt.title("Pie Chart: Purchases by City")
plt.show()

# ================== 4. STAIR CHART ==================
plt.figure()
plt.step(df["days_on_platform"], df["purchases"], where='mid')
plt.xlabel("Days on Platform")
plt.ylabel("Purchases")
plt.title("Stair Chart")
plt.show()

# ================== 5. HISTOGRAM ==================
plt.figure()
plt.hist(df["purchases"], bins=10)
plt.xlabel("Purchases")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

# ================== 6. MISSING VALUE CHART ==================
missing = df.isnull().sum()

plt.figure()
missing.plot(kind='bar')
plt.xlabel("Columns")
plt.ylabel("Missing Values")
plt.title("Missing Value Chart")
plt.show()

# ================== 7. OUTLIER (BOX PLOT) ==================
plt.figure()
plt.boxplot(df["purchases"])
plt.xlabel("Purchases")
plt.title("Outlier Detection (Box Plot)")
plt.show()