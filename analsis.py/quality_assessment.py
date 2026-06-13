from load_data import df

#Missing Values
print(df.isnull())

#Missing Value Percentage
print((df.isnull().sum() / len(df)) * 100) 

#Duplicate Records
print(df.duplicated().sum())

#Duplicate Records in specific column
print(df.duplicated(subset=['year']))

#unique values
for col in df.columns:
    print(col, df[col].nunique())

