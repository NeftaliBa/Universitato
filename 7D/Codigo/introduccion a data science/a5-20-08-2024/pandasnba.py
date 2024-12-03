import pandas as pd
from matplotlib import pyplot as plt

#datos = pd.read_csv("nba.csv", index_col = "Salary")
#jugador = datos.loc["Amir Johnson"]
#print(jugador)

datos = pd.read_csv("nba.csv")
dt_may = datos.sort_values(by="Salary", ascending=False).head(15)
new_dt = dt_may
x = new_dt['Name']
y = new_dt['Salary']

plt.figure(figsize=(10, 6))
bars = plt.bar(x, y, color="purple")


plt.xlabel('Jugadores')
plt.ylabel('Salario')
plt.title('Salario de jugadores')


plt.xticks(rotation=45, ha='right', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:,.0f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()


plt.show()