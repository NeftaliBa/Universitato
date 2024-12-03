import pandas as pd
import matplotlib.pyplot as plt

file_path = 'big_data/segunda parcial/a13-11-2024/prendas.csv'
df = pd.read_csv(file_path)

pivot_table = df.pivot_table(values='Item', index='Type', columns='Color', aggfunc='count')

pivot_table.plot(kind='bar', figsize=(10, 6))
plt.title('Prendas por Tipo y Color')
plt.xlabel('TDP')
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylabel('Cantidad')
plt.legend(title='Color')
plt.show()