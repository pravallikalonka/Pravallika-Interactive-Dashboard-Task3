import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('cleaned_housing_data.csv')

# Segment houses by furnishing status
segment_analysis = df.groupby('furnishingstatus')['price'].mean()
print("\nAverage Price by Furnishing Status:\n", segment_analysis)

# Bedroom segmentation
bedroom_analysis = df.groupby('bedrooms')['price'].mean()
print("\nAverage Price by Bedrooms:\n", bedroom_analysis)

# Visualization: Furnishing Status vs Price
segment_analysis.plot(kind='bar')
plt.title('Average House Price by Furnishing Status')
plt.xlabel('Furnishing Status')
plt.ylabel('Average Price')
plt.show()

# Visualization: Bedrooms vs Price
bedroom_analysis.plot(kind='bar')
plt.title('Average House Price by Bedrooms')
plt.xlabel('Bedrooms')
plt.ylabel('Average Price')
plt.show()