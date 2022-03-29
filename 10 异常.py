# 要引发异常，可使用raise语句，并将一个类（必须是Exception的子类）或实例作为参数
# 

# 引发通用异常，没有指出出现什么错误
# raise Exception 

# 以下添加了错误消息
# raise Exception('Hyperdrive overload')

"""
        一些内置的异常类
    类名                    描述
Exception           几乎所有异常类都由它派生而来
AttributeError      引用属性或给它赋值失败时引发
OSError             操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
IndexError          使用序列中不存在的索引时引发，为LookupError的子类
KeyError            使用映射中不存在的键时引发，为LookupError的子类
NameError           找不到变量名称时引发
SyntaxError         代码不正确时引发
TypeError           将内置操作或函数用于类型不正确的对象时引发
ValueError          将内置操作或函数用于这样的对象时引发：类型正确但包含的值不合适
ZeroDivisionError   在除法或求模运算的第二个参数为零时引发 
"""

# 自定义异常，需要直接或间接的继承Exception类
class SomeCustomException(Exception):
    # 也可以在自定义异常类中添加方法
    pass
# raise SomeCustomException('Hyperdrive overload')


# 捕获异常 使用try/except语句，见 10.1 异常示例.py
# 异常从函数向外传播到调用函数的地方，如果在这里也没有被捕获，异常将向程序的最顶层传播。
# 这意味着可使用try/except来捕获他人所编写的函数引发的异常

# 不提供参数的raise
class MuffledCalculator:
    muffled = False #True
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled: 
                # 启用抑制异常的功能后，打印一条错误消息，而不让异常继续传播
                print('Division by zero is illegal')
                # 此时方法将返回None，就不应该依赖返回值
            else:
                # 继续向上传播它
                # 如果无法处理异常，使用不带参数的raise通常是不错的选择
                # raise
                
                # 但有时你可能想引发别的异常，这种情况下进入except子句的异常将被作为异常上下文存储起来
                raise ValueError
                # 可使用raise ... from ... 语句提供自己异常的上下文，也可使用None来禁用上下文
                # raise ValueError from None

calculator = MuffledCalculator()
calculator.muffled = True
calculator.calc('10 / 0')

print('\nfinally子句')
# finally子句用于在异常时执行清理工作，确保代码块无论在是否引发异常时都执行
x = None
try:
    x = 1 / 1
except ZeroDivisionError:
    print("unknown varible")
finally:
    # 无论在是否引发异常时都执行
    print("Cleaning up ...")
    del x
# 若没有except语句(可以不写)，以上程序将在清理完成后崩溃
# finally子句非常适合用于确保文件或网络套接字等得以关闭
#     
# 有时候可使用条件语句来达成异常处理实现的目标，但这样编写出来的代码可能没那么自然，可读性也没那么高
# 使用条件判断时可能会重复查找两次（一次检查，一次获取）某个值，try/except直接尝试访问，无需检查，效率自然会高一些
# 当然效率可能提升不大，但使用try/except语句更自然，也更符合python的风格


