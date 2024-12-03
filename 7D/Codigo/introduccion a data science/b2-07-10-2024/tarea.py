import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

fruits = pd.read_csv('fruit_data_with_colours.csv')

target_fruits_name = dict(zip(fruits.fruit_label.unique(), fruits.fruit_name.unique()))

X = fruits[['mass', 'width', 'height']]
y = fruits['fruit_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

dato=[[20, 43, 5.5]]
fruit_prediction = knn.predict(dato)
predicted_fruit = target_fruits_name[fruit_prediction[0]]
print(f"Predi: {predicted_fruit}")

plt.figure(figsize=(10, 6))

colors = ['red', 'blue', 'green', 'orange']
for i, fruit_label in enumerate(target_fruits_name.keys()):
    fruit_data = fruits[fruits['fruit_label'] == fruit_label]
    plt.scatter(fruit_data['height'], fruit_data['mass'], 
                label=target_fruits_name[fruit_label], color=colors[i], s=50)

plt.scatter(dato[0][2], dato[0][0], color='black', marker='x', s=100, label='Predicción')
plt.xlabel('Altura')
plt.ylabel('Masa')
plt.legend()
plt.grid()
plt.show()
