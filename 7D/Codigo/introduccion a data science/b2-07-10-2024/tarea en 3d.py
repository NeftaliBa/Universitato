import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cargar datos
fruits = pd.read_csv('fruit_data_with_colours.csv')
print(fruits.head(10))

# Diccionario de etiquetas
target_fruits_name = dict(zip(fruits.fruit_label.unique(),
                              fruits.fruit_name.unique()))
print(target_fruits_name)

# Separar características y etiquetas
X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']

# Separar datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Inicializar y entrenar el clasificador KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Realizar predicción para un nuevo dato
new_data = [[20, 43, 5.5]]
fruit_prediction = knn.predict(new_data)
predicted_fruit = target_fruits_name[fruit_prediction[0]]
print(f"Predicción para el nuevo dato: {predicted_fruit}")

# Gráfica en 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Colores para cada tipo de fruta
colors = ['red', 'blue', 'green', 'orange']
for i, fruit_label in enumerate(target_fruits_name.keys()):
    fruit_data = fruits[fruits['fruit_label'] == fruit_label]
    ax.scatter(fruit_data['mass'], fruit_data['width'], fruit_data['height'],
               label=target_fruits_name[fruit_label], color=colors[i], s=30)

# Graficar el nuevo punto de predicción
ax.scatter(new_data[0][0], new_data[0][1], new_data[0][2],
           color='black', marker='x', s=100, label='Predicción')

# Etiquetas y leyenda
ax.set_xlabel('Masa')
ax.set_ylabel('Ancho')
ax.set_zlabel('Altura')
ax.legend()
plt.show()
