# Ejemplo de bar chart
from matplotlib import pyplot as plt

peliculas = ["Annie Hall", "Ben-Hur", "Cassablanca", "Gandhi", "West Side Story"]
oscares = [5, 11, 3, 8, 10]

xs = [ i + 0.1 for i, _ in enumerate(peliculas)]
plt.bar(xs, oscares)
plt.ylabel("Oscares ganados")
plt.xlabel("Peliculas")
plt.title("Peliculas mejores premiadas")
plt.xticks([i+0.5 for i, _ in enumerate(peliculas)], peliculas)
plt.show()