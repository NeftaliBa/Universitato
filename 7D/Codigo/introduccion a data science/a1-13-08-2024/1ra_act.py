# Ejemplo de Line chart
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
pib = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot (years, pib, color='blue', marker='x', linestyle='solid')
plt.title("Line chart del Producto Interno Bruto")
plt.ylabel("Billones de dolares")
plt.xlabel("Decadas")
plt.show()