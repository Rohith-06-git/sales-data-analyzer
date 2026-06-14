from load_data import df

import matplotlib.pyplot as plt


#Average Mileage
print(df['odometer'].mean())

# #Mileage by Brand
print(df.groupby('make')['odometer'].mean())

#Which brands remain in use longer?
print(df.groupby('make')['odometer'].mean().head(30).sort_values(ascending=False))

#Mileage vs Price
scatter_df = df[['odometer', 'sellingprice']].dropna()
scatter_df = scatter_df.sample(10000, random_state=42) #sampleData of 10000

plt.figure(figsize=(8,6))
plt.scatter(scatter_df['odometer'], scatter_df['sellingprice'] ,alpha = 0.3)
plt.title("Mileage vs price distribution")
plt.xlabel("odometer values")
plt.ylabel(" selling price of each brand")
plt.show()



