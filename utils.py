utils.py

# import libraries 
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
import numpy as np
import matplotlib.pyplot as plt

def df_info(dataframe):
  """Returns relative frequencies of unique values for given dataframe"""
  cols = dataframe.columns.to_list()
  for value in cols:
    print(dataframe[value].value_counts(normalize=True))
    print("========")
    print(f'Shape: {dataframe.shape}')

def return_feature_rank_from_RF(X_train,y_train):
# Build a forest and compute the impurity-based feature importances
    forest = ExtraTreesClassifier(n_estimators=20,random_state=0)
    forest.fit(X_train, y_train)
    importances = forest.feature_importances_
    std = np.std([tree.feature_importances_ for tree in forest.estimators_],axis=0)
    indices = np.argsort(importances)[::-1]

    # Print the feature ranking
    print("Feature ranking:")

    for f in range(X_train.shape[1]):
        print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

    # Plot the impurity-based feature importances of the forest
    plt.figure()
    plt.title("Feature importances")
    plt.bar(range(X_train.shape[1]), importances[indices],
            color="r", yerr=std[indices], align="center")
    plt.xticks(range(X_train.shape[1]), indices)
    plt.xlim([-1, X_train.shape[1]])
    plt.show()
    
    return (indices,importances)