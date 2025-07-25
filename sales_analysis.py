# sales_analysis.py

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("/content/Sales Data.csv")

# Display basic info
print("First 5 rows of the dataset:\n", df.head(5))
print(f"\nList of columns: {df.columns.tolist()}")
print(f"Shape of dataset (rows, columns): {df.shape}")

# Convert 'Order Date' to datetime and extract year
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Year'] = df['Order Date'].dt.year

# Drop missing values
df.dropna(inplace=True)

# Basic product stats
print("\nTotal number of products:", df["Product"].count())
print("\nProduct frequency:\n", df["Product"].value_counts())

# Product(s) with max quantity ordered
max_qty = df['Quantity Ordered'].max()
print("\nProduct(s) with max quantity ordered:\n", df[df['Quantity Ordered'] == max_qty])

# Top 5 most ordered products
top_ordered = df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 most ordered products:\n", top_ordered)

# Clean column if exists
if 'Hour' in df.columns:
    df.drop(columns=['Hour'], inplace=True)

# Product(s) with highest price
max_price = df['Price Each'].max()
print("\nProduct(s) with highest price:\n", df[df['Price Each'] == max_price])

# Top 5 (Product, Year) combinations by price frequency
top5_df = df.groupby(['Product', 'Year'])['Price Each'].count().sort_values(ascending=False).head(5).reset_index()
print("\nTop 5 (Product, Year) combinations with most prices:\n", top5_df)

# Visualizations
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Year", y="Month")
plt.title("Scatterplot of Year vs Month")
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Month', y='Product')
plt.title("Barplot of Product by Month")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Month', y='Quantity Ordered')
plt.title("Barplot of Quantity Ordered by Month")
plt.xticks(rotation=45)
plt.show()
