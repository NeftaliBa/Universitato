import pandas as pd
df = pd.read_csv('netflix_titles.csv')


#Estos venian en conjunto para la primera parte de la clase

#print(df.head(5).to_string())
#columns = list(df.columns)
#print(columns)
#print(df.isnull().mean())
#print(df.dtypes)

str_cols = list(df.columns)
str_cols.remove('release_year')

for i in str_cols:
    df[i] = df[i].str.strip()

print(df.head(5).to_string())