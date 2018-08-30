# -*- coding:utf-8 -*-
'''
try:
    <body>     包含了可能抛出异常的代码，当一个异常出现时，<body>中剩余代码被跳过。如果该异常匹配一个异常类型，那么该类型下的处理代码将被执行。
except <ExceptionType1>:
    <Handler1>   是处理异常的代码。
    ……
except <ExceptionTypeN>:
    <HandlerN>
except:
    <handleExcept>
else:
    <process_else>
finally:
    <process_finally>

1、首先，try和except之间的语句（即body）被执行。
2、如果没有异常出现，跳过except子句。
3、如果在执行try子句时出现异常，子句的剩余部分将会被跳过。
4、当一个异常出现时，如果异常类型匹配关键字except之后的异常名，那么这个except子句被执行，然后继续执行try语句之后的语句。
5、如果一个异常出现但是异常类型不匹配except子句中的异常名，那么这个异常被传递给这个函数的调用者；如果没有找到处理该异常的处理器，那么这是一个未处理异常且终止程序显示错误信息
6、多个except语句与elif语句类似
7、一个try语句可以有一个可选择的finally块，用来定义收尾动作，无论何种情况都会执行这个块。
且finally的执行，会在try的return之前执行，故实际应用中，不推荐在finally中使用return返回，
否则，无论如何，都是finally中的被返回
'''

def main():
    try:
        number1, number2 = eval(input("分别输入两个数字（用逗号隔开）："))
        result = number1 / number2
        print("它们的商是：", result)
    except ZeroDivisionError:
        print("除以0，错误！")
    except SyntaxError:
        print("数字间未输入逗号！")
    except:
        print("输入出错了！")
    else:
        print("没有错误！")
    finally:
        print("已执行完！")

main()

'''
try:
    <statements>            # main action
except <name1>:             # 当try中发生name1的异常时处理
    <statements> 
except (name2, name3):      # 当try中发生name2或name3中的某一个异常的时候处理
    <statements>
except <name4> as <data>:   # 当try中发生name4的异常时处理，并获取对应实例
    <statements>
except:                     # 其他异常发生时处理
    <statements>
else:                       # 没有异常发生时处理
    <statements>
finally:                    # 不管有没有异常发生都会处理
    <statements>
'''