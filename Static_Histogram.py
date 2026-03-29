import matplotlib.pyplot as plt

data = [12, 15, 14, 16, 18, 19, 20, 22, 24, 25, 25, 26, 28, 30]

plt.hist(data, bins=5, edgecolor='black')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.show()