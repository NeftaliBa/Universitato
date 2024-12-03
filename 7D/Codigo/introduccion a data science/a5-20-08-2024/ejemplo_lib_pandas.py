import pandas as pd

datos = {
"calorias": [420, 380, 390, 500, 400],
"duracion": [50, 40, 45, 60, 50]
}

# generar índices automáticamente como "dia 1", "dia 2", etc.
indices = [f"dia {i+1}" for i in range(len(datos['calorias']))]

# Crear el DataFrame con el índice personalizado
df = pd.DataFrame(datos, index=indices)

# Mostrar el DataFrame
print(df)
