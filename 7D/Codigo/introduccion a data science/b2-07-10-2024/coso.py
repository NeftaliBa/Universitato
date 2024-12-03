from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=150, n_features=2,centers=3,cluster_std=0.5,shuffle=True,random_state=0)


km = KMeans(n_clusters=3, init='random', n_init=20, max_iter=300, tol=1e-04, random_state=0)
y_km = km.fit_predict(X)


plt.scatter(X[y_km==0,0], X[y_km ==0,1], s=50, c='lightgreen', marker='s', label='cluster 1')
plt.scatter(X[y_km ==1,0], X[y_km ==1,1], s=50, c='orange', marker='o', label='cluster 2')
plt.scatter(X[y_km ==2,0], X[y_km ==2,1], s=50, c='lightblue', marker='v', label='cluster 3')
plt.legend()
plt.grid()
plt.show()