import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = pd.read_csv(r"oxigeno.csv")
df.head()
df.describe().T
df.isnull().any()
df_ = df[['Reduc_solidos','Reduc_doxigen']]
df_.head()

df_.hist()
plt.show()

plt.scatter(df_['Reduc_solidos'], df_['Reduc_doxigen'], color='red')
plt.xlabel("Reduc_solidos")
plt.ylabel("Reduc_doxigen")
plt.show()

plt.scatter(df_['Reduc_doxigen'], df_['Reduc_solidos'], color='blue')
plt.xlabel("Reduc_doxigen")
plt.ylabel("Reduc_solidos")
plt.show()

plt.scatter(df_['Reduc_solidos'], df_['Reduc_doxigen'], color='black')
plt.xlabel("Reduc_solidos")
plt.ylabel("Reduc_doxigen")
plt.show()

# Aqui inicia codigo de regresion lineal 
X = df_[['Reduc_solidos']]
y = df_[['Reduc_doxigen']]

reg_model = LinearRegression().fit(X, y)
reg_model.intercept_[0] + reg_model.coef_[0][0]*26.10

g = sns.regplot(x=X, y=y, scatter_kws={'color': 'b', 's': 9}, ci=False, color="r")
g.set_title(f'Model Equation: Reduc_doxigen = {round(reg_model.intercept_[0], 2)}'
            f' + Reduc_solidos*{round(reg_model.coef_[0][0],2)}')
g.set_ylabel('Reduc_doxigen')
g.set_xlabel('Reduc_solidos')
plt.show()