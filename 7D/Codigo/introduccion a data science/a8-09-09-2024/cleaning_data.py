
import pandas as pd
df = pd.read_csv('cleaning_dataFormateado.csv')
#df.dropna(inplace=True)
media = df["Calories"].mean()
moda = df["Calories"].mode()[0]
df.fillna({"Calories": media}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df.loc[22,'Date'] = '2020-12-22'
df.loc[7, 'Duration'] = 45
print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df.to_string())