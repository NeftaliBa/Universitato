import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

fruits = pd.read_csv('fruit_data_with_colours.csv')
target_fruits_name = dict(zip(fruits.fruit_label.unique(),
                              fruits.fruit_name.unique()))

X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

coso = [[200,8.4,7.3]]
fruit_prediction = knn.predict(coso)
predicted_fruit = target_fruits_name[fruit_prediction[0]]
print(f"Predicción: {predicted_fruit}")

plt.figure(figsize=(10, 6))
colors = ['red', 'blue', 'green', 'orange']
fig = ['*', 's', 'D', '^'] 

for i, (fruit_label, color, shape) in enumerate(zip(target_fruits_name.keys(), colors, fig)):
    fruit_data = fruits[fruits['fruit_label'] == fruit_label]
    plt.scatter(fruit_data['height'], fruit_data['mass'], label=target_fruits_name[fruit_label], color=color, s=50)

    centroid_height = fruit_data['height'].mean()
    centroid_mass = fruit_data['mass'].mean()
    plt.scatter(centroid_height, centroid_mass, color=color, marker=shape, s=200, edgecolor='black', label=f'Centroide {target_fruits_name[fruit_label]}')

plt.scatter(coso[0][2], coso[0][0], color='black', marker='x', s=100, label='Predicción')

plt.xlabel('Altura')
plt.ylabel('Masa')
plt.legend()
plt.grid()
plt.show()
