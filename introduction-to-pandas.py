
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

# Viewing and Selecting Data

top_five = car_sales.head()
print(f"top_five : \n {top_five}")

top_seven = car_sales.head(7)
print(f"top_seven: \n {top_seven}")

bottom_five = car_sales.tail()
print(f"bottom_five: \n {bottom_five}")

bottom_two = car_sales.tail(2)
print(f"bottom_two: \n {bottom_two}")

animals = pd.Series(['Dog', 'Pandas', 'Cat', 'fish'], index=[3, 9, 5, 3])
print(animals)

# .loc[] refers to index
loc_animal = animals.loc[3]
print(loc_animal)

loc_car = car_sales.loc[3]
print(loc_car)

# .iloc[] refers to position
i_loc_animal = animals.iloc[3]
print(i_loc_animal)

i_loc_car = car_sales.iloc[3]
print(i_loc_car)

up_to_position_x = animals.iloc[:3]
print(f"up to position x: \n {up_to_position_x}")

include_index_x = car_sales.loc[:3]  # car_sales.head(4)
print(f"include index x: \n {include_index_x}")

print_the_column = car_sales['Colour']  # car_sales.Colour
print(f'print the column: \n {print_the_column}')

select_specific_column1 = car_sales[car_sales['Make'] == 'Toyota']
print(f'select specific column: \n {select_specific_column1}')

select_specific_column2 = car_sales[car_sales['Odometer (KM)'] > 100000]
print(f'select specific column: \n {select_specific_column2}')






