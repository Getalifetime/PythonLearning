# 迭代(iterate)意味着重复多次，就像循环那样。之前使用for循环迭代过序列和字典，
# 实际上也可迭代其他对象：实现了方法__iter__的对象, 即迭代器

class Fibs:
    '表示斐波那契数列的迭代器'
    # 实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        # 调用方法__next__时，迭代器返回下一个值，若没有可供返回的值，应引发StopIteration异常
        self.a, self.b = self.b, self.a + self.b
        return self.a
    def __iter__(self):
        # 返回迭代器本身，这样迭代器就可直接用于for循环中
        return self
# 为什么不使用列表呢，例如有一个可逐个计算值的函数，可能只想逐个地获取值，而不是使用列表一次性的获取
# 如果有很多值，列表可能占用太多内存。如果有无穷个值，则列表长度需要无穷大，例如上面的斐波那契数列，必须使用迭代器实现



fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

# 通过对可迭代对象使用内置函数iter，可获得一个迭代器
it = iter([1, 2, 3])
print(it.__next__())
# 可使用内置的便利函数next，在这种情况下，next(it)与it.__next__()等效
print(next(it))
print(next(it))
# print(next(it)) # StopIteration

# 从迭代器创建序列
# 除了对迭代器和可迭代对象进行迭代（通常这样做）之外，还可将它们转换为序列
# 在可以使用序列的情况下,大多也可使用迭代器或可迭代对象(索引和切片等操作除外)
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self

ti = TestIterator()
seq = list(ti)
print(seq)
