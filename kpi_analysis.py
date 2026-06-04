import pandas as pd

# Load dataset
df = pd.read_csv('cleaned_housing_data.csv')

# KPI Calculations
average_price = df['price'].mean()
maximum_price = df['price'].max()
minimum_price = df['price'].min()
average_area = df['area'].mean()
average_bedrooms = df['bedrooms'].mean()
average_bathrooms = df['bathrooms'].mean()

print("--- Key Performance Indicators ---")
print(f"Average House Price: {average_price}")
print(f"Maximum House Price: {maximum_price}")
print(f"Minimum House Price: {minimum_price}")
print(f"Average Area: {average_area}")
print(f"Average Bedrooms: {average_bedrooms}")
print(f"Average Bathrooms: {average_bathrooms}")