import matplotlib.pyplot as plt

x = []
y = []

n = int(input("Enter number of data points: "))

for i in range(n):
    x_val = int(input(f"Enter X value {i+1}: "))
    y_val = int(input(f"Enter Y value {i+1}: "))
    
    x.append(x_val)
    y.append(y_val)

plt.plot(x, y, marker='o')

plt.xlabel("X values (Independent Variable)")
plt.ylabel("Y values (Dependent Variable)")
plt.title("Dynamic X-Y Axis Data Plot")

plt.grid(True)

plt.show()