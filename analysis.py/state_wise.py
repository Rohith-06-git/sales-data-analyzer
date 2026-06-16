from load_data import df

#Sales by State
print(df['state'].value_counts())

#Average Price by State
print(df.groupby('state')['sellingprice'].mean().to_frame())


