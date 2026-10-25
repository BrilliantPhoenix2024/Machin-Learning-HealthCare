
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Two main datatypes:

# series -> 1-dimensional
series = pd.Series(['BMW', 'Honda', 'Toyota'])
print(series)

colours = pd.Series(['Blue', 'Red', 'White'])
print(colours)

# dataframe -> 2-dimensional
car_data = pd.DataFrame({'car make': series, 'Colour': colours})
print(car_data)

# Import a DataFrame
car_sales = pd.read_csv('car-sales.csv')
print(car_sales)

# Exporting a DataFrame
car_sales.to_csv('exported_car_sales.csv', index=False)
exported_car_sales = pd.read_csv('exported_car_sales.csv')
print('**************')
print(exported_car_sales)






