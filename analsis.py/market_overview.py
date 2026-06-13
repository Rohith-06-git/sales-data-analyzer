from load_data import df

#Cars Sold by Year
print(df['year'].value_counts().sort_index())

#Top Brands
print(df['make'].value_counts().head(20))

#Top Models
print(df['model'].value_counts().head(20))

#Body Type Analysis
print(df['body'].value_counts().head(20))