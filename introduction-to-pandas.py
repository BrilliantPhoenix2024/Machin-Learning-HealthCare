
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

# Describing Data
car_sales_dataType = car_sales.dtypes
print(car_sales_dataType)

car_sales_columns = car_sales.columns
print(car_sales_columns)

car_sales_index = car_sales.index
print(car_sales_index)

car_sales_describtion = car_sales.describe()
print(car_sales_describtion)

# car_sales_information = car_sales.info()
# print(car_sales_information)

car_prices = pd.Series([3000, 1500, 500])
print('**************')
print(car_prices.mean())

# car_sales.sum()
car_doors_sum = car_sales['Doors'].sum()
print(car_doors_sum)

length = len(car_sales)
print(length)






