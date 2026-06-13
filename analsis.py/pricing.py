from load_data import df
import matplotlib.pyplot as plt

#Selling Price Statistics
print(df['sellingprice'].describe())

#Most Expensive Brands
meb = df.groupby('make')['sellingprice'].mean().sort_values(ascending=False)
print(meb)

#Most Expensive Models
mem = df.groupby('model')['sellingprice'].mean().sort_values(ascending=False)
print(mem)

#Most vehicles sold under what price ?
print(df['sellingprice'].value_counts().head(20))

#Price Distribution - Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['sellingprice'], bins=100)

plt.title("Distribution of Car Selling Prices")
plt.xlabel("Selling Price")
plt.ylabel("Number of Cars Sold")

plt.show()