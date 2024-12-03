import pandas as pd

df = pd.read_csv('netflix_titles.csv')
columnas = df.columns.tolist()

tipos_columnas = df.dtypes
print("Tipos de datos, columna:\n", tipos_columnas)

valores_perdidos = df.isnull().sum()
print("\nValores perdidos por columna:\n", valores_perdidos)

columnas_con_valores_perdidos = df.columns[df.isnull().any()].tolist()

columnas_solo_cadenas = []
columnas_mixtas = []

for col in columnas_con_valores_perdidos:
    if df[col].apply(lambda x: isinstance(x, str) or pd.isnull(x)).all():
        columnas_solo_cadenas.append(col)
    else:
        columnas_mixtas.append(col)

print("\nColumnas solo con cadenas:\n", columnas_solo_cadenas)
print("\nColumnas mixtas (números y cadenas):\n", columnas_mixtas)
df[columnas_solo_cadenas] = df[columnas_solo_cadenas].fillna("dato no disponible")

for col in columnas_solo_cadenas:
    df[col] = df[col].apply(lambda x: x.strip() if isinstance(x, str) else x)

valores_validos_rating = ['PG-13', 'PG', 'TV-MA', 'TV-PG', 'TV-14', 'TV-Y', 'R', 'TV-G', 'TV-Y7', 'G', 'NC-17', 'NR', '', 'TV-Y7-FV']
df['rating'] = df['rating'].apply(lambda x: x if x in valores_validos_rating else 'NR')
df['country'] = df['country'].replace({
    'East Germany': 'Germany',
    'West Germany': 'Germany',
    'Soviet Union': 'Russia'
})

df.to_csv('ntl.csv', index=False)
