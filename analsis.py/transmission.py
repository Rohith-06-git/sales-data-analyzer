from load_data import df

#Manual vs Automatic
print(df['transmission'].value_counts())

#Average Price
print(df.groupby('transmission')['sellingprice'].mean().to_frame())

#Average Mileage of Transmission
print(df.groupby('transmission')['odometer'].mean().to_frame())
