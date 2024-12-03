import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

dataframe = pd.read_csv(r"analisis.csv")
#print(dataframe.head(20))
#print(dataframe.describe())

X = np.array(dataframe[["op","ex","ag"]])
y = np.array(dataframe['categoria'])
print(X.shape)

plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')
asignar = []
ax.set_xlabel('Op')
ax.set_ylabel('Ex')
ax.set_zlabel('Ag')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=dataframe['categoria'], s=60)
plt.show()

KMeans = KMeans(n_clusters=9).fit(X)
centroids = KMeans.cluster_centers_
#print(centroids)
labels = KMeans.predict(X)
C = KMeans.cluster_centers_
fig = plt.figure()
ax =fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=dataframe['categoria'], s=60)
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=dataframe['categoria'], s=1000)
plt.show()


