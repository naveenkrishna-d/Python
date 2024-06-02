import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(0,10,100)
y= np.sin(x)

plt.figure(figsize=(10,5))
plt.plot(x,y,label='Sine Wave')
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

# Creating a bar chart
categories = ['A', 'B', 'C']
values = [10, 20, 15]

plt.figure(figsize=(7, 5))
plt.bar(categories, values, color='skyblue')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

x = np.random.rand(50)
y = np.random.rand(50)

plt.figure(figsize=(7, 5))
plt.scatter(x, y, color='green')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()