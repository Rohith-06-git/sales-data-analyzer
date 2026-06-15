from load_data import df

#Compare MMR and Actual Selling Price
df['price_diff'] = df['sellingprice'] - df['mmr']
print(df['price_diff'])

#Brand-wise Difference
print(df.groupby('make')['price_diff'].mean().to_frame())
