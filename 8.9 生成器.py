# 生成器是一种使用普通函数语法定义的迭代器。
# 生成器和迭代器是近年来引入的最强大功能。
# 虽然生成器能让你编写出非常优雅的代码，但请放心，无论编写什么程序，都可以完全不使用生成器

# 创建一个将嵌套列表展开的函数
from matplotlib.pyplot import close


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element 

# 包含yield语句的函数都被称为生成器。
# 生成器的行为与普通函数截然不同，差别在于：生成器不使用return返回一个值，而是可以生成多个值，每次一个。
# 每次使用yield生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒。
# 被重新唤醒后，函数将从停止的地方开始继续执行

# 为使用所有的值，可对生成器进行迭代
nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print(num)

# 递归式生成器，可处理任意层嵌套的列表
def recurflatten1(nested):
    try:
        for sublist in nested:
            for element in recurflatten1(sublist):
                yield element
    except TypeError:
        # 基线条件下，要求这个函数展开单个元素，这时for循环将引发TypeError异常
        yield nested

seq = [[[1], 2], 3, 4, [5, [6, 7]], 8]
# for num in recurflatten(seq):
#     print(num)
print(list(recurflatten1(seq)))
# 然而，这个解决方案存在一个问题。如果nested是字符串或类似于字符串的对象，它就属于序列，不会引发TypeError异常
# 首先，我们想将类似字符串的对象视为原子值，不想将其展开
# 其次，这样的对象进行迭代会导致无穷递归，因为字符串的第一个元素是一个长度为1的字符串，而长度为1的字符串的第一个元素就是字符串本身
# 因此必须在生成器开头进行检查，要检查对象是否类似于字符串，最简单最快捷的方式是尝试将对象与一个字符串拼接起来
# 并检查这是否会引发TypeError异常
def recurflatten2(nested):
    try:
        # 不迭代类似字符串的对象
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        
        for sublist in nested:
            for element in recurflatten2(sublist):
                yield element
    except TypeError:
        yield nested

seq2 = ['foo', ['bar', ['baz']]]
print(list(recurflatten2(seq)))
print(list(recurflatten2(seq2)))

# 生成器由两个单独的部分组成：生成器函数和生成器的迭代器
# 生成器的函数是由def语句定义的，其中包含yield
# 生成器的迭代器是这个函数返回的结果。
print(flatten)
print(flatten(nested))

# 生成器的方法
# 生成器开始运行后，可使用生成器和外部之间的通信渠道向它提供值。这个通信渠道包含两个端点
# 1外部世界：可访问生成器的方法send，这个方法接受一个参数 —— 要发送的消息，可以是任何对象
# 2生成器：在挂起的生成器内部，yield可能用作表达式而不是语句。换言之，当生成器重新运行时，
#   yield返回一个值 —— 通过send从外部世界发送的值。如果使用next，yield将返回None

# 仅当生成器被挂起（即遇到第一个yield）后，使用send才有意义。要在此之前向生成器提供信息，可使用生成器的函数的参数
# 如果一定要在生成器刚启动时对其调用方法send，可向它传递参数None
def repeater(value):
    while True:
        new = (yield value) # 如果要以某种方式返回值，不管三七二十一，将其用圆括号括起来吧
        if new is not None:
            value = new
        

r = repeater(12)
print(next(r))

print(r.send("Hello World!"))

# 生成器还包括另外两种方法：
# throw：用于在生成器中（yield处）引发异常，调用时可提供一个异常类型、一个可选值和一个traceback对象
# close：用于停止生成器，调用时无需提供任何参数。
#       将在yield处引发GenerateorExit异常，因此若要在生成器中提供一些清理代码，可将yield放在try/finally语句中