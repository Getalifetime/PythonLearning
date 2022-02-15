"""
######列表######
"""
# 在Python中，用方括号[]来表示列表，并用逗号来分隔其中的元素
numbers = ['1', '2', '3', '4', '5', '6', '7']
# 通过将索引指定为-1 ，可让Python返回最后一个列表元素
# 这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。
# 这种约定也适用于其他负数索引，例如，索引-2 返回倒数第二个列表元素，索引-3 返回倒数第三个列表元素，以此类推。
print("\n列表：")
print("Python将打印列表的内部表示：", end = '')
print(numbers)
print('请求列表元素时，Python只返回该元素，而不包括方括号和引号：',end='')
print(numbers[0])
print('numbers[-1] =',numbers[-1])
print('numbers[-2] = %s' %numbers[-2])

### 修改、添加和删除元素
# 你创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。
# 在列表末尾增加元素
numbers.append("8")
numbers.append(9)
numbers.append("新增10")
print("\n使用append()方法在列表末尾增加元素：")
print(numbers)
print(numbers[-1])
print('\n使用insert()方法在列表中插入元素:')
numbers.insert(0,'0')
print(numbers)
print('\n使用del删除元素:')
del(numbers[4])
print(numbers)
del numbers[-1]
print(numbers)
# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；
# 如果你要在删除元素后还能继续使用它，就使用方法pop()
print('\n使用方法pop() 删除元素，并使用其值:')
a = numbers.pop()
print('删除列表末尾的元素['+str(a)+']列表变为:')
print(numbers)
print('弹出列表中任意位置的元素:')
a = numbers.pop(-1)
print('弹出最后位置的'+ str(a)+'后')
print(numbers)
a = numbers.pop(0)
print('弹出第一个位置的'+ str(a)+'后')
print(numbers)


print('\n根据值删除元素:')
# 有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()
# 方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
numbers.remove("1")
print(numbers)

print("\n可以将任何东西加入列表中，其中的元素之间可以没有任何关系")
mix_list = []
mix_list.append(1)
mix_list.append(2.5)
mix_list.append('A')
mix_list.append('@')
print(mix_list)

# 创建一个空列表，将长度初始化为10
sequence = [None] * 10
print(sequence)

"""
######组织列表######
"""
# 使用方法sort() 对列表进行永久性排序
# 使用函数sorted() 对列表进行临时排序
cars = ['bmw', 'audi', 'honda', 'toyota', 'vw', 'jeep', 'tesla', 'ford', 'mercedes benz', 'porsche', '1']
cars.insert(1,'mazda')
print('\n使用函数sorted() 对列表进行临时排序: ')
print(sorted(cars))
print('The original list: ')
print(cars)

print("\n使用方法sort() 对列表进行永久性排序")
cars.sort()
print('The original list after sort:')
print(cars)
cars.sort(reverse=True)
print('The reversed sort list:')
print(cars)

# 倒着打印表，反转列表元素的排列顺序，方法reverse() 永久性地修改列表元素的排列顺序
#cars = ['bmw', 'audi', 'honda', 'toyota', 'vw', 'jeep', 'buick', 'ford', 'mercedes benz', 'porsche', '1', 'B']
print("\n使用方法reverse反转列表元素排列顺序")
print("The original list: ",cars)
cars.reverse()  
print('\nThe reverse list: ', cars) # reverse直接修改列表，不返回任何值

print("\n使用函数len()获取列表的长度:")
print('\nThe length of the list: ' + str(len(cars)))
# 当列表为空时，这种访问最后一个元素的方式会导致错误，需要判断列表长度
print("判断列表长度后再打印最后一个元素:")
cars = []
if len(cars) > 0:
    print(cars[-1])
else:
    print("列表为空")

####################
######遍历列表######
####################
# 这行代码让Python从列表cars 中取出一个名字，并将其存储在变量car 中，对于用于存储列表中每个值的临时变量，可指定任何名称。
# for 语句末尾的冒号告诉Python，下一行是循环的第一行。
cars = ['bmw', 'audi', 'honda', 'toyota', 'vw', 'jeep', 'ford', 'mercedes benz', 'porsche']
for car in cars: #冒号告诉Python，下一行是循环的第一行
    print(car.upper())
    print("The "+ car.title() + " is a car brand\n")
# 每个缩进的代码行都是循环的一部分，Python将执行整个循环直到列表中没有其他的值
print("I can't wait to see your new car!")

###################################################################################
#Python通过使用缩进让代码更易读，简单的说，它强制要求你使用缩进让代码整洁而结构清晰
###################################################################################



########################
######创建数值列表######
########################
print("\n创建数值列表")
# 函数range() 让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）。
print('使用函数range()')
for num in range(1,5): 
    print(num, end=' ')

print('\n使用函数list()将range()的结果直接转换为列表')
num_list = list(range(1,6))
print(num_list)

# 使用函数range() 时，还可指定步长，如10以内的奇数
print("range()设定步长")
num_list = list(range(1,10,2))
print(num_list)


squares = []
for value in range(1,11):
    squares.append(value**2)
print("使用range函数和append方法创建数值列表：")
print('平方数:', squares)
print("对数字列表执行简单的统计计算：")
print('最小值:', min(squares))
print("最大值:", max(squares))
print("累加和:", sum(squares))

###列表解析
# 列表解析 将for 循环和创建新元素的代码合并成一行，并自动附加新元素。
print('\n列表解析方式创建列表:')
squares = [value**2 for value in range(1,11)]
print(squares)
cubes = [value**3 for value in range(1,11)]
print(cubes)
binpowers = [2**value for value in range(1,11)]
print(binpowers)

###使用列表的一部分————Python称之为“切片”
# 要创建切片，可指定要使用的第一个元素和最后一个元素的索引
print('\n切片：')
print(squares[1:5])
# 没有指定起始索引，Python将自动从列表头开始
print(cubes[:4])
# 要让切片终止与列表末尾，也可用类似的语法
print(cubes[4:])
print("输出binpowers最后3个：")
print(binpowers[-3:])

print('\n遍历切片：')
for val in binpowers[2:8]:
    print(val, end = ", ")
print('\n')

###复制列表
# 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。
# 这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。
print("\n使用切片复制列表，而不能简单的直接赋值：")
binpowers_1 = binpowers[:] #将得到两个列表
binpowers_2 = binpowers    #简单的赋值并不能得到两个列表，这种语法是让Python将新变量cubes_2关联到包含在cubes中的列表，因此这两个变量都指向同一个列表

print('binpowers = ',binpowers)
for i in range(-6,0):
    if (len(binpowers) >= (-i)):
        binpowers.pop(i)
    else:
        print("!!WARNING!! 超出列表长度, i = ", i)
print('修改后binpowers = ',binpowers)    
print('原始列表的修改不会影响binpowers_1 = ',binpowers_1)
print('但会影响binpowers_2 = ',binpowers_2)


