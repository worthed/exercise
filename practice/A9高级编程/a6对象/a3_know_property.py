# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/5 下午4:32
IDE：PyCharm
描述：了解python的属性
"""
# ############### 定义 ###############
# 定义时，在普通方法的基础上添加 @property 装饰器；
# 定义时，属性仅有一个self参数
class Foo:

    def func(self):
        pass

    # 定义属性
    @property
    def prop(self):
        pass
# ############### 调用 ###############
# 调用属性时，无需括号
foo_obj = Foo()
foo_obj.func()
foo_obj.prop   #调用属性


'-1-属性定义方式'
'-①-装饰器方式：在类的普通方法上应用@property装饰器'
# 经典类，具有一种@property装饰器（如上一步实例）
# 新式类（ 如果类继object，那么该类是新式类 ），具有三种@property装饰器
class Goods(object):

   def __init__(self):
       # 原价
       self.original_price = 100
       # 折扣
       self.discount = 0.8

   @property
   def price(self):
       # 实际价格 = 原价 * 折扣
       new_price = self.original_price * self.discount
       return new_price

   @price.setter
   def price(self, value):
       self.original_price = value

   @price.deleter
   def price(self):
       del self.original_price

obj = Goods()
price = obj.price         # 获取商品价格
print(price)
obj.price = 200   # 修改商品原价
print(obj.price)
del obj.price     # 删除商品原价


'-②-装饰器方式：静态字段方式，创建值为property对象的静态字段'
class Goods_2(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')
    '''
    第一个参数是方法名，调用 对象.属性 时自动触发执行方法
    第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
    第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
    第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息
    '''
obj2 = Goods_2()
print(obj2.PRICE)         # 获取商品价格
obj2.PRICE = 200   # 修改商品原价
print(obj2.PRICE)
del obj2.PRICE     # 删除商品原价