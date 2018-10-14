# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/19 上午10:37
IDE：PyCharm
描述：回归树算法
https://github.com/tushushu/imylu/
"""
from copy import copy
from practice.A11算法.a3回归树.utils import list_split

# 1、创建Node类
# 初始化，存储预测值、左右结点、特征和分割点
class Node(object):

    def __init__(self, score=None):
        self.score = score
        self.left = None
        self.right = None
        self.feature = None
        self.split = None


# 2、创建回归树类
# 初始化，存储根节点和树的高度。
class RegressionTree(object):

    def __init__(self):
        self.root = Node()
        self.depth = 1
        self._rules = None


    # 3、计算分割点、MSE
    # 根据自变量X、因变量y、X元素中被取出的行号idx，列号feature以及分割点split，计算分割后的MSE。
    # 注意这里为了减少计算量，用到了方差公式：
    def _get_split_mse(self, X, y, idx, feature, split):
        split_sum = [0, 0]
        split_cnt = [0, 0]
        split_sqr_sum = [0, 0]

        for i in idx:
            xi, yi = X[i][feature], y[i]
            if xi < split:
                split_cnt[0] += 1
                split_sum[0] += yi
                split_sqr_sum[0] += yi ** 2
            else:
                split_cnt[1] += 1
                split_sum[1] += yi
                split_sqr_sum[1] += yi ** 2

        split_avg = [split_sum[0] / split_cnt[0], split_sum[1] / split_cnt[1]]
        split_mse = [split_sqr_sum[0] - split_sum[0] * split_avg[0],
                     split_sqr_sum[1] - split_sum[1] * split_avg[1]]
        return sum(split_mse), split, split_avg


    # 4、计算最佳分割点
    # 遍历特征某一列的所有的不重复的点，找出MSE最小的点作为最佳分割点。如果特征中没有不重复的元素则返回None
    def _choose_split(self, X, y, idx, feature):

        unique = set([X[i][feature] for i in idx])
        if len(unique) == 1:
            return None

        unique.remove(min(unique))
        mse, split, split_avg = min(
            (self._get_split_mse(X, y, idx, feature, split)
             for split in unique), key=lambda x: x[0])

        return mse, feature, split, split_avg


    # 5、选择最佳特征
    # 遍历所有特征，计算最佳分割点对应的MSE，找出MSE最小的特征、对应的分割点，左右子节点对应的均值和行号。
    # 如果所有的特征都没有不重复元素则返回None
    def _choose_feature(self, X, y, idx):
        m = len(X[0])

        split_rets = map(lambda j: self._choose_split(X, y, idx, j), range(m))
        split_rets = filter(lambda x: x is not None, split_rets)

        return min(split_rets, default=None, key=lambda x: x[0])


    # 6、规则转文字
    # 将规则用文字表达出来，方便我们查看规则
    def _expr2literal(self, expr):

        feature, op, split = expr
        op = ">=" if op == 1 else "<"
        return "Feature%d %s %.4f" % (feature, op, split)

    # 7、获取规则
    # 将回归树的所有规则都用文字表达出来，方便我们了解树的全貌。
    # 这里用到了队列+广度优先搜索。有兴趣也可以试试递归或者深度优先搜索
    def _get_rules(self):

        que = [[self.root, []]]
        self._rules = []

        while que:
            nd, exprs = que.pop(0)
            if not (nd.left or nd.right):
                literals = list(map(self._expr2literal, exprs))
                self._rules.append([literals, nd.score])

            if nd.left:
                rule_left = copy(exprs)
                rule_left.append([nd.feature, -1, nd.split])
                que.append([nd.left, rule_left])

            if nd.right:
                rule_right = copy(exprs)
                rule_right.append([nd.feature, 1, nd.split])
                que.append([nd.right, rule_right])


    # 8、训练模型
    # 仍然使用队列 + 广度优先搜索，训练模型的过程中需要注意：
    #   1.控制树的最大深度max_depth；
    #   2.控制分裂时最少的样本量min_samples_split；
    #   3.叶子结点至少有两个不重复的y值；
    #   4.至少有一个特征是没有重复值的
    def fit(self, X, y, max_depth=5, min_samples_split=2):

        idxs = list(range(len(y)))
        que = [(self.depth + 1, self.root, idxs)]

        while que:
            depth, nd, idxs = que.pop(0)

            if depth > max_depth:
                depth -= 1
                break

            if len(idxs) < min_samples_split or \
                    set(map(lambda i: y[i], idxs)) == 1:
                continue

            split_ret = self._choose_feature(X, y, idxs)
            if split_ret is None:
                continue

            _, feature, split, split_avg = split_ret

            nd.feature = feature
            nd.split = split
            nd.left = Node(split_avg[0])
            nd.right = Node(split_avg[1])

            idxs_split = list_split(X, idxs, feature, split)
            que.append((depth + 1, nd.left, idxs_split[0]))
            que.append((depth + 1, nd.right, idxs_split[1]))

        self.depth = depth
        self._get_rules()

    # 9、打印规则
    # 模型训练完毕，查看一下模型生成的规则
    @property
    def rules(self):

        for i, rule in enumerate(self._rules):
            literals, score = rule
            print("Rule %d: " % i, ' | '.join(
                literals) + ' => y_hat %.4f' % score)

    # 10、预测一个样本
    def _predict(self, Xi):

        nd = self.root
        while nd.left and nd.right:
            if Xi[nd.feature] < nd.split:
                nd = nd.left
            else:
                nd = nd.right
        return nd.score

    # 11、预测多个样本
    def predict(self, X):
        return [self._predict(Xi) for Xi in X]

