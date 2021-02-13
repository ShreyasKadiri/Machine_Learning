#Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
df.head()

df.info()
df.describe()
df
df.shape


#Univariate Analysis
df_setosa=df.loc[df['species'] == 'setosa']
df_setosa

df_virginica=df.loc[df['species']=='virginica']
df_virginica

plt.plot(df_setosa['sepal_length'], np.zeros_like(df_setosa['sepal_length']), 'o')
plt.plot(df_virginica['sepal_length'], np.zeros_like(df_virginica['sepal_length']),'o')
plt.xlabel("Sepal Length")
plt.show()

#Bivariate Analysis
sns.FacetGrid(df,hue="species",size=5).map(plt.scatter,"petal_length","sepal_width").add_legend();
plt.show()

#Multivariate Analysis
sns.pairplot(df,hue="species",size=3)





