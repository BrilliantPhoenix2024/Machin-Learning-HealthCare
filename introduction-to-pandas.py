
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

# crosstab()
compare_two_columns = pd.crosstab(car_sales['Make'], car_sales['Doors'])
print(f'compare two columns: \n {compare_two_columns}')


# Groupby()
group_by_specific_column = car_sales.groupby(['Make']).mean(numeric_only=True)
print(group_by_specific_column)

# Plot the Odometer column
car_sales['Odometer (KM)'].plot()
# Add a title and labels
plt.title("Car Mileage")
plt.xlabel("Car Index")
plt.ylabel("Odometer (KM)")

# Display the graph
plt.show()


car_sales['Odometer (KM)'].hist()
plt.show()


# Remove $ and commas from prices
car_sales["Price"] = (
    car_sales["Price"]
    .str.replace(r"[$,]", "", regex=True)
    .astype(float)
    .astype(int)
)

car_sales["Price"].plot()
plt.show()


# Manipulating Data
car_sales['Make'] = car_sales['Make'].str.lower()
car_sales_missing = pd.read_csv('car-sales-missing-data.csv')
print(car_sales_missing)

car_sales_missing['Odometer'] = car_sales_missing['Odometer'].fillna(car_sales_missing['Odometer'].mean())
print(car_sales_missing)


# Remove rows containing missing values
car_sales_missing_dropped = car_sales_missing.dropna()

print("##############")
print(car_sales_missing_dropped)

# Export to CSV
car_sales_missing_dropped.to_csv(
    "car-sales-missing-dropped.csv",
    index=False
)

print("CSV file exported successfully!")


# Column from Series
seats_column = pd.Series([5, 5, 5, 5, 5])

# Create a new Seats column
car_sales["Seats"] = seats_column

# Replace missing values with 5
car_sales["Seats"] = car_sales["Seats"].fillna(5)

print("@@@@@@@@@")
print(car_sales)

# Create a new column from a Python list
fuel_economy = [7.5, 9.2, 5.0, 8.7, 5.6, 9.5, 4.7, 2.6, 6.1, 3.0]

car_sales["Fuel per 100KM"] = fuel_economy

print("!!!!!!!!!!!")
print(car_sales)

car_sales['Total fuel used (L)'] = car_sales['Odometer (KM)'] / 100 * car_sales['Fuel per 100KM']
print('&&&&&&&&&&&')
print(car_sales)

# Create a column from a single value
car_sales['Number of wheels'] = 4
print('&&&&&&&&&&&')
print(car_sales)

# Removing a column
car_sales.drop('Seats', axis=1, inplace=True)
print('&&&&&&&&&&&')
print(car_sales)



