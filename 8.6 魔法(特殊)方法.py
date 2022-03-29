# Python中有些方法名称很特别，开头和结尾都是两个下划线，其中很大一部分都是魔法（特殊）方法
# 如果对象实现了这些方法，它们将在特定情况下被Python调用而几乎不需要直接访问

# 1 构造函数 __init__ 在对象创建后自动调用

# 2 元素访问：一组可以创建行为类似于序列或映射的对象的魔法方法
# 2.1 __len__(self): 返回集合包含的项数。对序列来说为元素个数，对映射来说为键-值对数
# 2.2 __getitem__(self, key): 返回与指定键相关联的值。对序列来说，键为0~n-1的整数（n为序列长度，为负整数时，应从末尾往前数）。对映射来说，键可以是任何类型
# 2.3 __setitem__(self, key, value): 与键相关联的方式存储值，以便以后能使用__getitem__来获取
# 2.4 __delitem__(self, key): 在对对象的组成部分使用__del__语句时被调用，删除与key相关联的值
def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError

class ArithmeticSequence:
    """
    实现一个算数序列
    没有方法__len__, 因为其长度是无穷的
    要禁止删除元素，因此没有实现__del__
    """
    def __init__(self, start=0, step=1):
        """
        初始化这个算数序列
        start   -序列中的第一个值
        step    -两个相邻值的差
        changed -一个字典，包含用户修改后的值，初始为空
        """
        self.start = start
        self.step = step
        self.changed = {}
    
    def __getitem__(self, key):
        """
        从算数序列中获取一个元素
        """
        check_index(key)

        try:
            return self.changed[key] # 若用户修改过此值，则返回修改后的值
        except KeyError:
            return self.start + key * self.step # 没有修改或就计算元素的值
    
    def __setitem__(self, key, value):
        """
        修改算数序列中的元素
        """
        check_index(key)

        self.changed[key] = value
    
s = ArithmeticSequence(1, 2)
print(s[4])
s[4] = 0
print(s[4])
print(s[5])
# print(s['a'])
# print(s[-1])

# 序列还有很多有用的魔法方法和普通方法，要实现所有这些方法，不仅工作量大，且难度不小
# 如果只想定制某种操作行为，就没有理由去重新实现其他所有方法。因此可以继承

# 要实现一种行为类似于内置列表的序列类型，可直接继承list
class CounterList(list):
    '一个带访问计数器的列表'
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0
    
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)
        # 注意，重写__getitem__并不一定保证会捕捉用户所有的访问操作，因为还有其他访问列表内容的方式如方法pop

cl = CounterList(range(10))
print("\n CounterList:")
print(cl)
print(cl.counter)

print(cl[1])    # 访问一次元素后计数器加1
print(cl.counter) 

print(cl[2] + cl[4])    
print(cl.counter)   # 访问两次元素后计数器就加2

# CounterList继承了list的方法
cl.reverse()
print(cl)
print(cl.counter)

del cl[3:6]
print(cl)
print(cl.counter)

# 3 其他魔法方法
# 魔法方法有很多，大多是为非常高级的用途准备的，可参阅Python Reference Manual的Special method names一节