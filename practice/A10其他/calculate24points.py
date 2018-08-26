# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/24 上午11:08
IDE：PyCharm
描述：计算24点
思路：
1、枚举4个数字可以组成的所有的算式，找到其中等于24的式子
2、对于每一个算式，用一棵二叉树来存取。根节点保存运算符（+,-,*,/）
3、左子树保存运算符左侧的子算式，右子树保存运算符右侧的子算式，运算结果也存在根节点中
"""
import math
import itertools

# 节点类
class Node(object):
    def __init__(self, result=None):

        """
        如果 _operator 是None，则 _result 就是数字本身，
        如果 _operator 不为None，则 _result 表示的是左右两棵子树运算的结果
        :param result:
        """
        self._left = None
        self._right = None
        self._operator = None # 操作符
        self._result = result

    def set_expression(self, left_node, right_node, operator):
        self._left = left_node
        self._right = right_node
        self._operator = operator
        expression = "{} {} {}".format(left_node._result, operator, right_node._result)
        self._result = eval(expression)

    def __repr__(self):
        if self._operator:
            return '<Node operator="{}">'.format(self._operator)
        else:
            return '<Node value="{}">'.format(self._result)

def get_expression(tree):
    if tree._operator == None:
        return str(tree._result)
    left_expression = get_expression(tree._left)
    right_expression = get_expression(tree._right)
    expression = "({} {} {})".format(left_expression, tree._operator, right_expression)
    return expression

def build_tree(left_tree, right_tree):
    """
    build_tree 中会枚举所有的运算方式，组成新的二叉树并返回所有可能的组合
    :param left_tree:
    :param right_tree:
    :return:
    """
    treelist = []
    tree1 = Node()
    tree1.set_expression(left_tree, right_tree, "+")
    treelist.append(tree1)
    tree2 = Node()
    tree2.set_expression(left_tree, right_tree, "-")
    treelist.append(tree2)
    tree4 = Node()
    tree4.set_expression(left_tree, right_tree, "*")
    treelist.append(tree4)
    # 运算方式是除法，除数也就是右侧子算式的结果不能为0
    if right_tree._result != 0:
        tree5 = Node()
        tree5.set_expression(left_tree, right_tree, "/")
        treelist.append(tree5)
    return treelist

def build_all_trees(array):
    """
    创建二叉树
    :param array: 输入一个数字
    :return: 所有可能的算式
    """
    if len(array) == 1:
        tree = Node(array[0])
        return [tree]

    treelist = []
    # 第一层for循环中将这组数字，拆成左右两部分，分别对应左右两棵子树的部分
    for i in range(1, len(array)):
        left_array = array[:i]
        right_array = array[i:]
        left_trees = build_all_trees(left_array)
        right_trees = build_all_trees(right_array)
        # 对于给定的左子树和右子树，build_tree 函数用加减乘除把它们连接在一起，组成新的二叉树
        for left_tree in left_trees:
            for right_tree in right_trees:
                combined_trees = build_tree(left_tree, right_tree)
                treelist.extend(combined_trees)
    return treelist


def find_24(questions):
    for question in questions:
        perms = itertools.permutations(question)
        found = False
        for perm in perms:
            treelist = build_all_trees(perm)
            for tree in treelist:
                if math.isclose(tree._result, 24, rel_tol=1e-10):
                    expression = get_expression(tree)
                    print(expression)
                    found = True
                    break
            if found:
                break

if __name__ == "__main__":
    questions = [
        [7,7,3,3],
        [8,3,8,3],
        [5,1,5,5],
        [10,10,4,4],
        [1,5,7,10],
        [4,7,8,10],
        [2,2,3,10],
        [2,4,10,10],
        [9,10,6,9],
        [4,4,7,7],
        [1,4,5,6],
        [2,5,5,10]
    ]
    find_24(questions)


