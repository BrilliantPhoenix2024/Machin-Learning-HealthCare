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
nut_butter_price = {
    'Almond_butter': 8,
    'Peanut_butter': 10,
    'Cashew_butter': 12
}
fig5, axes7 = plt.subplots()
axes7.bar(nut_butter_price.keys(), nut_butter_price.values())
axes7.set(
    title='Store',
    xlabel='Butter Type',
    ylabel='Price ($)'
)
plt.show()

# 6. Histograms And Subplots
fig6, axes8 = plt.subplots()
axes8.barh(list(nut_butter_price.keys()), list(nut_butter_price.values()))

# Make some data for Histogram
x = np.random.randn(1000)
fig7, axes9 = plt.subplots()
axes9.hist(x)
plt.show()

# Two options for subplots
# Subplot option 1
# Plot to each different axes
# Create 4 subplots
fig, ((axes0, axes1), (axes2, axes3)) = plt.subplots(
    nrows=2,
    ncols=2,
    figsize=(10, 8)
)

# Plot 1: Line
axes0.plot(x, x / 2)
axes0.set(title='Line Plot')

# Plot 2: Scatter
axes1.scatter(np.random.random(10), np.random.random(10))
axes1.set(title='Scatter Plot')

# Plot 3: Bar
axes2.bar(nut_butter_price.keys(), nut_butter_price.values())
axes2.set(title='Bar Plot')

# Plot 4: Histogram
axes3.hist(np.random.randn(1000))
axes3.set(title='Histogram')

# Adjust spacing
fig.tight_layout()

# Show all plots together
plt.show()

# Subplot option 2
# Create 4 subplots
fig8, axes5 = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

# Subplot option 2
# Create 4 subplots
# Plot to each different index
axes5[0, 0].plot(x, x/2)
axes5[0, 1].scatter(np.random.random(10), np.random.random(10))
axes5[1, 0].bar(nut_butter_price.keys(), nut_butter_price.values())
axes5[1, 1].hist(np.random.randn(1000))

fig8.tight_layout()
plt.show()


# Plotting from Pandas DataFrame
car_sales = pd.read_csv('car-sales.csv')
print(car_sales)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2020', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()

car_sales['Price'] = car_sales['Price'].str.replace(
    r'[$,.]', '', regex=True
)

# Remove last two zeros
car_sales['Price'] = car_sales['Price'].str[:-2]
car_sales['Sale Date'] = pd.date_range('1/1/2020', periods=len(car_sales))
car_sales['Total Sales'] = car_sales['Price'].astype(int).cumsum()
print(car_sales)

# Let's plot the total sales
car_sales.plot(x='Sale Date', y='Total Sales')
plt.show()

# Reassign Price column to int
car_sales['Price'] = car_sales['Price'].astype(int)

# Plot scatter plot with price column as numeric
car_sales.plot(x='Odometer (KM)', y='Price', kind='scatter')
plt.show()

# Create a bar Graph DataFrame
x = np.random.rand(10, 4)

# Turn it into a DataFrame
df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])

df.plot.bar()
plt.show()

car_sales.plot(x='Make', y='Odometer (KM)', kind='bar')
plt.show()

car_sales['Odometer (KM)'].plot.hist()
plt.show()

car_sales['Odometer (KM)'].plot.hist(bins=20)
plt.show()

heart_disease = pd.read_csv('heart-disease.csv')
print(heart_disease.head())

# Create a Histogram of age
heart_disease['age'].plot.hist(bins=30)
plt.show()

heart_disease.plot.hist(figsize=(10, 30), subplots=True)
plt.show()


