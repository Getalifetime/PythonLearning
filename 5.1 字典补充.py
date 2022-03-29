"""
映射：通过名称来访问各个值的数据结构
字典是Python中唯一的内置映射类型，其中的值不安顺序排列，而是存储在键下。
键可以是数字、字符串或元组。在映射中，键必须是独一无二的
键-值对称为项
"""
"""
字典的一些用途：
1.表示棋盘的状态，其中每个键都是由坐标组成的元组
2.存储文件修改时间，其中的键为文件名
3.数字电话/地址簿
"""
from copy import deepcopy

# 函数dict 可从其他映射或键-值对序列创建字典
items = [('name', 'Bob'), ('age', 42)]
d = dict(items)
print(d)
print(d['name'])
# 使用关键字实参来调用dict
d = dict(name='Alice', age=30)
print(d)
# 若没有提供任何实参，将返回一个空字典
d = dict()
print(d)

"""
键的类型：键可以是任何不可变的类型，如浮点数（实数）、字符或元组
自动添加：直接给字典中原本没有的键赋值就会创建一个新项，不需使用append或其他方法
成员资格：字典中查找（key in dict）的是键而不是值，而列表中查找（value in list）的是值而不是索引
         相比于检查列表是否包含指定的值，检查字典包含指定的键效率更高，且数据结构越大，效率差距就越大
"""
# 元组中只包括像数字和字符串这样的不可变参数，才可以作为字典中有效的键
# 例如表示棋盘的状态或坐标的值
x = {
    (0,0):-1,
    (0,1):0,
    (0,2):0,
    (1,0):1,
    (1,1):1,
    (8,8):-1
}
print('\n元组作为字典的键')
print(x)
print(x[(1,0)])

## 字典方法
#1 clear
x = {}
y = x
x['key'] = 'value'
print('\n#1')
print(y)
x = {} # 此操作只是将x指向一个新的空字典，而原来的字典没有任何改变
print(y)

x['key'] = 'value'
y = x
x.clear() #删除原来字典的所有元素
print(y)

#2 copy 返回一个新字典，其包含的键值对与原来字典相同，但执行的是浅复制，因为值本身是原件，不是副本
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz'] }
y = x.copy()
y['username'] = 'user1' #当替换副本中的值时，原件不受影响
y['machines'].remove('bar') #当修改副本中的值时，原件也将发生变化，因为原件指向的也是被修改的值
print('\n#2')
print(x)
print(y)
# 为避免以上问题，一种办法是执行深复制，即同时复制键及其包含的所有值，使用模块copy中的函数deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(c)
print(dc)

#3 fromkeys创建一个新字典，其中包含指定的键，且每个键对应的值都是None
d = dict.fromkeys(['name', 'age'])
print('\n#3')
print(d)
# 若不想使用默认值，可提供特定的值
d = dict.fromkeys(['name', 'age'], '(unknown)')
print(d)

#4 get为访问字典项提供了宽松的环境。通常，试图访问字典中没有的项时将引发错误，而使用get则不会这样
print('\n#4')
print(d.get('gender')) #不指定默认值时则返回None
print(d.get('gender', 'N/A')) #指定默认值
print(d.get('name', 'N/A')) #字典中包含指定的键时，get与普通字典查找相同

## 创建一个简单的电话簿数据库，支持按姓名查询
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23',
    },

    'Bob': {
        'phone': '9102',
        'addr': 'Bar Street 42',
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90',
    },
}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('Enter the name you are searching: ')
# 方法1，处理不存在的值
"""
while True:
    request = input('Phone number (p) or address (a)?')
    if request == 'p' or request == 'P':
        key = 'phone'
        break
    elif request == 'a' or request == 'A':
        key = 'addr'
        break
if name.title() in people:
    print("{}'s {} is {}.".format(name.title(), labels[key], people[name.title()][key]))
else:
    print(name + " is not in the database!")
"""

# 方法2 使用get提供默认值
request = input('Phone number (p) or address (a)?')
key = request
if request == 'p' or request == 'P':
    key = 'phone'
elif request == 'a' or request == 'A':
    key = 'addr'

person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

print("{}'s {} is {}".format(name, label, result))

#5 items返回一个包含所有字典项的列表，注意字典项在列表中排列顺序不固定
dict_pyweb = {
    'title': 'Python Web Site',
    'url': 'http://www.python.org',
    'spam': 0
}
it = dict_pyweb.items() # 返回值属于一种名为 字典视图 的特殊类型
print('\n#5')
print(it)
print(len(it)) #确定其长度（字典项数）
print(('spam',0) in it) #执行成员资格检查
# 视图的一个优点是不复制，他们始终是底层字典的反映，即使修改了底层字典亦如此
dict_pyweb['spam'] = 1
print(('spam',0) in it)
print(('spam',1) in it)
list_pyweb = list(dict_pyweb.items()) #将字典项复制到列表中
print(list_pyweb) 

#6 keys返回一个字典视图，其中包含指定字典中的键
print('\n#6')
print(dict_pyweb.keys())

#7 pop用于获取与指定键相关联的值，并将该键值对从字典中删除
val = dict_pyweb.pop('spam')
print('\n#7')
print(val)
print(dict_pyweb)

#8 popitem 随机弹出一个字典项，因为字典项的顺序是不确定的。不同于list.pop弹出最后一个元素
val = dict_pyweb.popitem()
print('\n#8')
print(val)
print(dict_pyweb)

#9 setdefault 与get相似，也获取指定的键相关联的值。但若字典不包含指定的键，则在字典中添加指定的键值对
dict_pyweb.setdefault('url', 'http://www.python.org')
dict_pyweb.setdefault('spam', 0)
print('\n#9')
print(dict_pyweb)
val = dict_pyweb.setdefault('spam', 1) #指定值已存在则返回其值
print(val)
print(dict_pyweb)

#10 update使用一个字典中的项来更新另一个字典
x = {'changed': 'Feb 15 2022 13:23:35'}
dict_pyweb.update(x)
print('\n#10')
print(dict_pyweb)

#11 values 返回一个由字典中的值组成的字典视图，因此可能会包含重复的值
d = {1:1, 2:2, 3:3, 4:1}
print('\n#11')
print(d.values())


## 字典推导
squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
print(squares[5])
print(squares)