import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier

dataSet=pd.read_csv("/diabetic_data.csv")
dataSet.replace('?', np.NAN, inplace=True)

freqColumn=dataSet.count()
freqColumn

for ds in dataSet.columns:
    dataSet[ds]=dataSet[ds].fillna(dataSet[ds].value_counts().mode()[0])
for ds in dataSet.columns:
    dataSet[ds]=dataSet[ds].astype('category').cat.codes

for ds in dataSet.columns:
    mean = dataSet[ds].mean()
    sd = dataSet[ds].std()
    dataSet = dataSet[(dataSet[ds] <= mean+(3*sd))]

correlationOfColumns = dataSet.corr()
plt.figure(num=None, figsize=(20, 20), dpi=80, facecolor='w', edgecolor='k')
sns.heatmap(correlationOfColumns,cmap="Greens")

correlationOfColumns

correlationOfLabels=correlationOfColumns.iloc[-1]
for key,value in correlationOfLabels.items():
    if abs(value)<0.02:
        dataSet.drop(key,inplace=True,axis=1)

classifier = MLPClassifier(solver="lbfgs",alpha=1e-4,hidden_layer_sizes=(100,50,3),random_state=42,max_iter=5000)
y=dataSet["readmitted"]
x=dataSet.drop("readmitted",axis=1)
scores=cross_val_score(classifier,x,y,cv=10)
print('Cross-validation scores:', scores)
print('Mean score:', scores.mean())

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

"""creating the model and training it"""

clustering=KMeans(n_clusters=3, random_state=42, n_init="auto")
clustering.fit(dataSet)

score=silhouette_score(dataSet,clustering.labels_)
score
