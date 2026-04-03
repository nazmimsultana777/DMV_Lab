import pandas as pd

import matplotlib.pyplot as plt
df = pd.read_csv("clv_data.csv")


df = df.head(30)


print ("Dataset:")

print(df)

data = df["purchases"]

plt.figure()
plt.boxplot(data)

plt. xlabel("Purchases")
plt. ylabel("Values")
plt. title("Box Plot for Purchases")


plt. show()