import pandas as pd
import matplotlib.pyplot as plt


prendas_df = pd.read_csv('prendas.csv')
tipo_counts = prendas_df.groupby('Type').size()
color_counts = prendas_df.groupby('Color').size()

tipo_counts.plot(kind='bar', color='blue', title='Cantidad de prendas por tipo')
plt.xlabel('Tipo de prenda')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylabel('Cantidad')
plt.show()

color_counts.plot(kind='bar', color='purple', title='Cantidad de prendas por color')
plt.xlabel('Color')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylabel('Cantidad')
plt.show()
