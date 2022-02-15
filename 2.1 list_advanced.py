# 使用字符串创建字符列表可方便的修改字符串
print("\n使用list()创建字符列表")
print(list("Hello"))
name = list('Perl')
name[2:] = list('ar')
print(name)
# 通过使用切片赋值，可将切片替换为长度与其不同的序列
name[1:] = list("ython")
print(name)

# 将字符列表转换为字符串
print(''.join(name))

# 切片赋值在不替换原有元素的情况下插入新元素
numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers)

# 采用相反的方式删除切片
numbers[1:4] = [] # 等同于del numbers[1:4]
print(numbers)

# 方法clear清空列表
print(numbers.clear())

# 方法count计算指定的元素在列表中出现的次数
lst = ['to', 'be', 'or', 'not', 'to', 'be']
print(lst.count('to'))

# 方法extend将多个值附加到列表末尾，可使用一个列表扩展另一个列表
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
# 或使用切片达到同样的效果，但可读性不高
a = [1, 2, 3]
a[len(a):] = b
print(a)

# 方法index在列表中查找指定值的第一次出现的索引
print(lst.index('or'))

# 入栈和出栈（LIFO后进先出），可使用append和pop
x = [1, 2, 3]
x.append(x.pop())
print(x)

# 队列操作（FIFO先进先出）可使用insert(0, ...)代替append，
# 或用pop(0)替代pop()
# 一种更佳的解决方案是使用模块collections中的deque

# 方法remove删除第一个为指定值的元素
lst.remove('to')
print(lst)

# 方法sort用于对列表进行就地排序，不返回任何值
x = [4, 2, 1, 6, 9, 7]
### y = x.sort() wrong!!
y = x.copy()
y.sort()
print(x)
print(y)

# 为了获取排序后列表的副本，另一个方式是使用函数sorted
# 该函数可用于任何序列，总是返回一个列表
y = sorted(x)
print(x)
print(y)
p = sorted("python")
print(p)
# 方法sort和函数sorted都接受两个可选参数：key和reverse
# 要根据长度对元素进行排序，可将参数key设置为函数len
x = ['333', '22', '1', '6666', '94123412', '7435234']
x.sort(key=len)
print(x)
# 在很多情况下，将参数key设置为一个自定义函数很有用

# 函数reversed按相反的顺序迭代序列，它不返回列表，而是返回一个迭代器
print(list(reversed(p))) # 可使用list将返回的对象转换为列表