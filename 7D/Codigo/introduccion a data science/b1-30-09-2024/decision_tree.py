from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import  DecisionTreeClassifier
from sklearn import tree

#cargamos el dataset de las flores
iris = datasets.load_iris()
x = iris.data
y = iris.target

#creamos el clasificador del arbol
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(x,y)

#imprimimos el arbol
text_representation = tree.export_text(clf)
print(text_representation)

fig = plt.figure(figsize=(25,26))
_ = tree.plot_tree(clf,
                   feature_names= iris.feature_names,
                   class_names=iris.target_names,
                   filled=True)
fig.savefig("decision_tree.png")

