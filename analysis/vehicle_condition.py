from load_data import df

#Average Price by Condition
print(df.groupby('condition')['sellingprice'].mean())

#Condition Distribution
print(df['condition'].value_counts().sort_index())