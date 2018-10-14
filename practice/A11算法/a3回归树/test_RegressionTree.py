# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/19 上午11:24
IDE：PyCharm
描述：
"""
from practice.A11算法.a3回归树.utils import load_boston_house_prices, \
    train_test_split, get_r2, run_time
from practice.A11算法.a3回归树.RegressionTrees import RegressionTree


@run_time
def main():
    print("Tesing the accuracy of RegressionTree...")
    # Load data
    X, y = load_boston_house_prices()
    # Split data randomly, train set rate 70%
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=10)
    # Train model
    reg = RegressionTree()
    reg.fit(X=X_train, y=y_train, max_depth=3)
    # Show rules
    reg.rules
    # Model accuracy
    get_r2(reg, X_test, y_test)


if __name__ == "__main__":
    main()
