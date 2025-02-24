import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.plot()
plt.show()

plt.plot([1, 2, 3, 4])
plt.show()

x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
plt.plot(x, y)
plt.show()

# 1st Method:
# Creates a figure
fig1 = plt.figure()
# Adds some axes
ax = fig1.add_subplot()
plt.show()

# 2end Method:
# Create a figure
fig2 = plt.figure()
axes1 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
axes1.plot(x, y)
plt.show()

# 3rd Method:
fig3, axes2 = plt.subplots()
axes2.plot(x, [20, 50, 100, 250])
plt.show()

# Matplotlib example workflow
# 1- Prepare some data

a = [1, 2, 3, 4]
b = [11, 22, 33, 44]

# 2- Setup plot
fig4, axes3 = plt.subplots(figsize=(10, 10))

# 3- Plot data
axes3.plot(x, y)

# 4- Customize plot
axes3.set(title='Simple Plot', xlabel='x-axis', ylabel='y-axis')

# 5- Save and Show ( save the whole figure)
fig4.savefig('./sample-plot.png')


# Making figures with NumPy arrays
# Create some data
x = np.linspace(0, 10, 100)
print(x[:10])

# Create a line plot
fig1, axes4 = plt.subplots()
axes4.plot(x, x**2)
plt.show()

# Create a Scatter plot
fig2, axes5 = plt.subplots()
axes5.scatter(x, np.exp(x))
plt.show()

fig4, axes6 = plt.subplots()
axes6.scatter(x, np.sin(x))
plt.show()

# Create a plot form a Dictionary
nu_butter_price = {
    'Almond_butter': 8,
    'Peanut_butter': 10,
    'Cashew_butter': 12
}
fig5, axes7 = plt.subplots()
axes7.bar(nu_butter_price.keys(), nu_butter_price.values())
axes7.set(
    title='Store',
    xlabel='Butter Type',
    ylabel='Price ($)'
)
plt.show()








