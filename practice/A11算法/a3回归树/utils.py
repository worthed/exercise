# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/19 上午11:21
IDE：PyCharm
描述：
"""
import os
from random import random, seed, randint
from time import time
from math import exp
from copy import copy
from statistics import median

BASE_PATH = os.path.split(os.path.realpath(__file__))[0]


def load_data(file_name):
    """Read csv file.
    Arguments:
        file_name {str} -- csv file name
    Returns:
        X {list} -- 2d list object with int or float
        y {list} -- 1d list object with int or float
    """

    path = os.path.join(BASE_PATH, "dataset", "%s.csv" % file_name)
    f = open(path)
    X = []
    y = []
    for line in f:
        line = line[:-1].split(",")
        xi = [float(s) for s in line[:-1]]
        yi = line[-1]
        if '.' in yi:
            yi = float(yi)
        else:
            yi = int(yi)
        X.append(xi)
        y.append(yi)
    f.close()
    return X, y


def load_breast_cancer():
    """Load breast cancer data for classification.
    Returns:
        X {list} -- 2d list object with int or float
        y {list} -- 1d list object with int or float
    """

    return load_data("breast_cancer")


def load_boston_house_prices():
    """Load boston house prices data for regression.
    Returns:
        X {list} -- 2d list object with int or float
        y {list} -- 1d list object with int or float
    """

    return load_data("boston_house_prices")


def min_max_scale(X):
    """Scale the element of X into an interval [0, 1].
    Arguments:
        X {list} -- 2d list object with int or float
    Returns:
        list -- 2d list object with float
    """

    m = len(X[0])
    x_max = [-float('inf') for _ in range(m)]
    x_min = [float('inf') for _ in range(m)]
    for row in X:
        x_max = [max(a, b) for a, b in zip(x_max, row)]
        x_min = [min(a, b) for a, b in zip(x_min, row)]
    ret = []
    for row in X:
        tmp = [(x - b)/(a - b) for a, b, x in zip(x_max, x_min, row)]
        ret.append(tmp)
    return ret


def train_test_split(X, y, prob=0.7, random_state=None):
    """Split X, y into train set and test set.
    Arguments:
        X {list} -- 2d list object with int or float
        y {list} -- 1d list object with int or float
    Keyword Arguments:
        prob {float} -- Train data expected rate between 0 and 1 (default: {0.7})
        random_state {int} -- Random seed (default: {None})
    Returns:
        X_train {list} -- 2d list object with int or float
        X_test {list} -- 2d list object with int or float
        y_train {list} -- 1d list object with int 0 or 1
        y_test {list} -- 1d list object with int 0 or 1
    """

    if random_state is not None:
        seed(random_state)
    X_train = []
    X_test = []
    y_train = []
    y_test = []
    for i in range(len(X)):
        if random() < prob:
            X_train.append(X[i])
            y_train.append(y[i])
        else:
            X_test.append(X[i])
            y_test.append(y[i])
    # Make the fixed random_state random again
    seed()
    return X_train, X_test, y_train, y_test


def get_acc(clf, X, y):
    """Calculate the prediction accuracy of classification model.
    Arguments:
        clf {model} -- classification model
        X {list} -- 2d list object with int or float
        y {list} -- 1d list object with int
    Returns:
        float
    """

    acc = sum((yi_hat == yi for yi_hat, yi in zip(clf.predict(X), y))) / len(y)
    print("Test accuracy is %.3f%%!" % (acc * 100))
    return acc


def run_time(fn):
    """Decorator for calculating function runtime.Depending on the length of time,
    seconds, milliseconds, microseconds or nanoseconds are used.
    Arguments:
        fn {function}
    Returns:
        function
    """

    def wrapper():
        start = time()
        fn()
        ret = time() - start
        if ret < 1e-6:
            unit = "ns"
            ret *= 1e9
        elif ret < 1e-3:
            unit = "us"
            ret *= 1e6
        elif ret < 1:
            unit = "ms"
            ret *= 1e3
        else:
            unit = "s"
        print("Total run time is %.1f %s" % (ret, unit))
    return wrapper


def get_r2(reg, X, y):
    """Calculate the goodness of fit of regression model.
    Arguments:
        reg {model} -- regression model
        X {list} -- 2d list object with int or float
        y {list} -- 1d list object with int
    Returns:
        float
    """

    sse = sum((yi_hat - yi) ** 2 for yi_hat, yi in zip(reg.predict(X), y))
    y_avg = sum(y) / len(y)
    sst = sum((yi - y_avg) ** 2 for yi in y)
    r2 = 1 - sse/sst
    print("Test r2 is %.3f!" % r2)
    return r2


def sigmoid(x, x_min=-100):
    """Calculate the sigmoid value of x.
    Sigmoid(x) = 1 / (1 + e^(-x))
    Arguments:
        x {float}
    Keyword Arguments:
        x_min {int} -- It would cause math range error when x < -709 (default: {-100})
    Returns:
        float -- between 0 and 1
    """

    return 1 / (1 + exp(-x)) if x > x_min else 0


def split_list(X, idxs, feature, split, low, high):
    """ Sort the list, if the element in the array is less than result index,
    the element value is less than the split. Otherwise, the element value is
    equal to or greater than the split.
    Arguments:
        X {list} -- 2d list object with int or float
        idx {list} -- indexes, 1d list object with int
        feature {int} -- Feature number
        split {float} -- The split point value
    Returns:
        int -- index
    """

    p = low
    q = high - 1
    while p <= q:
        if X[idxs[p]][feature] < split:
            p += 1
        elif X[idxs[q]][feature] >= split:
            q -= 1
        else:
            idxs[p], idxs[q] = idxs[q], idxs[p]
    return p


def list_split(X, idxs, feature, split):
    """Another implementation of "split_list" function for performance comparison.
    Arguments:
        nums {list} -- 1d list with int or float
        split {float} -- The split point value
    Returns:
        list -- 2d list with left and right split result
    """

    ret = [[], []]
    while idxs:
        if X[idxs[0]][feature] < split:
            ret[0].append(idxs.pop(0))
        else:
            ret[1].append(idxs.pop(0))
    return ret


def _test_split_list(iterations=10**4, max_n_samples=1000, max_n_features=10, max_element_value=100):
    """Test correctness and runtime efficiency of both split_list functions.
    _split_list takes about 2.4 times as split_list does.
    Keyword Arguments:
        iterations {int} -- How many times to iterate. (default: {10**4})
        max_arr_len {int} -- Max random length of array (default: {1000})
        max_num {int} -- Max value of array's elements (default: {100})
    """

    time_1 = time_2 = 0
    for _ in range(iterations):
        n = randint(1, max_n_samples)
        m = randint(1, max_n_features)
        X = [[randint(1, max_element_value) for _ in range(m)]
             for _ in range(n)]
        idxs_1 = list(range(n))
        idxs_2 = copy(idxs_1)
        feature = randint(1, m) - 1
        split = median(map(lambda i: X[i][feature], range(n)))
        low = 0
        high = n

        start = time()
        ret_1 = split_list(X, idxs_1, feature, split, low, high)
        time_1 += time() - start

        start = time()
        ret_2 = list_split(X, idxs_2, feature, split)
        time_2 += time() - start

        assert all(i_1 == i_2 for i_1, i_2 in zip(
            sorted(idxs_1[low:ret_1]), sorted(ret_2[0])))
        assert all(i_1 == i_2 for i_1, i_2 in zip(
            sorted(idxs_1[ret_1:high]), sorted(ret_2[1])))

    print("Test passed!")
    print("split_list runtime for %d iterations  is: %.3f seconds" %
          (iterations, time_1))
    print("_split_list runtime for %d iterations  is: %.3f seconds" %
          (iterations, time_2))


def get_euclidean_distance(arr1, arr2):
    """Calculate the Euclidean distance of two vectors.
    Arguments:
        arr1 {list} -- 1d list object with int or float
        arr2 {list} -- 1d list object with int or float
    Returns:
        float -- Euclidean distance
    """

    return sum((x1 - x2) ** 2 for x1, x2 in zip(arr1, arr2))


def gen_data(low, high, n_rows, n_cols=None):
    """Generate dataset randomly.
    Arguments:
        low {int} -- The minimum value of element generated.
        high {int} -- The maximum value of element generated.
        n_rows {int} -- Number of rows.
        n_cols {int} -- Number of columns.
    Returns:
        list -- 1d or 2d list with int
    """
    if n_cols is None:
        ret = [randint(low, high) for _ in range(n_rows)]
    else:
        ret = [[randint(low, high) for _ in range(n_cols)]
               for _ in range(n_rows)]
    return ret


