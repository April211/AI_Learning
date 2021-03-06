import sys, os
import numpy as np
sys.path.append(os.getcwd() + r'\Modules')
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import Linear_Regression_SGD_Class as lrsgd
import matplotlib.pyplot as plt


def process_features(X):
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X = scaler.fit_transform(X)
    m, n = X.shape
    X = np.c_[np.ones((m, 1)), X]
    return X
# end


housing = fetch_california_housing()
X = housing.data
y = housing.target.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X_train = process_features(X_train)
X_test = process_features(X_test)

eta1 = 1
N = 700
eta1_list = np.empty(shape=(1, 0))
r2_list = np.empty(shape=(1, 0))
N_list = np.empty(shape=(1, 0))

# 固定 N = 8000，测试 eta_1
for i in range(70):
    model1 = lrsgd.LinearRegressionSGD()
    model1.fit(X_train, y_train, eta1, 8000)
    y_pred = model1.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    eta1_list = np.append(eta1_list, eta1)
    r2_list = np.append(r2_list, r2)
    # print("mse = {}, r2 = {}.".format(mse, r2))
    print(eta1)
    eta1 += 4

fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].set_title('r2 ~ eta_1', size=20)
axs[0].plot(eta1_list, r2_list, c='b', linewidth=2)

r2_list = np.empty(shape=(1, 0))

# 固定 eta = 50，测试 N
for i in range(40):
    model2 = lrsgd.LinearRegressionSGD()
    model2.fit(X_train, y_train, 140, N)
    y_pred = model2.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    N_list = np.append(N_list, N)
    r2_list = np.append(r2_list, r2)
    # print("mse = {}, r2 = {}.".format(mse, r2))
    print(N)
    N += 400

axs[1].set_title('r2 ~ N', size=20)
axs[1].plot(N_list, r2_list, c='g', linewidth=2)

plt.show()