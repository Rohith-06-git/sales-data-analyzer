from load_data import df

#Top Sellers
print(df['seller'].value_counts().head(20).to_frame())

#Revenue by Seller
print(df.groupby('seller')['sellingprice'].sum().sort_values(ascending=False).to_frame())

