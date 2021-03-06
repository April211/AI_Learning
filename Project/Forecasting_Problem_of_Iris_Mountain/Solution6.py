import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn import datasets
from sklearn.model_selection import train_test_split
import Logistic_Stepwise as lrs


def process_features(X):
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]
    return X
# end


iris = datasets.load_iris()
X = iris["data"]
y = (iris["target"]==2).astype(np.int).reshape(-1, 1)       # 列向量
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

X_train = process_features(X_train)
X_test = process_features(X_test)

model = lrs.LogisticStepwise()
model.forward_selection(X_train, y_train, eta_0=10, eta_1=50, N=20000)
proba = model.predict_proba(X_test)
entropy = model.cross_entropy(y_test, proba)

print("Cross entropy = {}.".format(entropy))
