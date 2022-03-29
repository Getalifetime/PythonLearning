from math import sqrt


'''if语句'''


cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':    #在Python中检查是否相等时区分大小写
        print(car.upper())
    else:
        print(car.title())
        
if 'Honda' not in cars:
    print("we will add 'Honda' into the list: ")
    cars.append('Honda')
    print(cars)
'''
# 如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，而只想检查变量的值，可将变量的值转换为小写，再进行比较
# 使用and 检查多个条件：age >= 18 and age <= 21
# 使用or 检查多个条件:age < 18 or age > 21
# 判断特定的值是否已包含在列表中，可使用关键字in:'Honda' in cars
# 确定特定的值未包含在列表中，可使用关键字not in：'Honda' not in cars
'''
#
print("\n布尔表达式:")
car = 'subaru'
print("Is car == 'subaru'?")
print(car == 'subaru')

print("Is car == 'audi'? ")
print(car == 'audi')
#
print('\n确定列表不是空的')
somethings = []
if somethings:
    print('We do have someting.')
else:
    print('We have nothing.')
#
print("\nif-elif-else 结构:")
age = 16
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: # Python并不要求if-elif 结构后面必须有else 代码块。
    price = 0
print("Your admission cost is $" + str(price) + ".")

#另一种实现
if age < 4 or age >= 65:
    price = 0
elif age >= 4 and age < 18:# 或使用链式比较 4 <= age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

#if处理多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
print("\nStarting to make your pizza.")
for toppings in requested_toppings:
    if toppings in available_toppings:
        print ("Add " + toppings + '.')
    else:
        print("Sorry, "+ toppings + " are not available now.")
print("Finished making your pizza.")


# 条件表达式—— C语言中三目运算符的python版本
a = 3
b = 3 if a > 1 else 2
print(b)

a = 1
b = 3 if a > 1 else 2
print(b)

# is运算符，检查两个对象是否相同而不是相等
x = y = [1, 2, 3] # 链式赋值
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)

# 使用内置函数zip进行并行迭代
names = ['anne', 'beth', 'cris', 'david']
ages = [12, 15, 32, 44]
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old.')

# 迭代时获取索引, 内置函数enumerate生成可迭代的‘索引-值’对
for index, name in enumerate(names):
    if 'cris' == name.lower():
        names[index] = 'chris'
    elif 'bob' == name.lower():
        pass    # pass 什么都不做
    elif 'anne' == name.lower():
        print("Welcome!")
print(names)

# 有时候肯能想动态的编写python代码，并将其作为语句进行执行或作为表达式进行计算
# 使用exec和eval执行字符串及计算其结果
sting = "print('Hello, world!')"
exec(sting) # 函数exec将字符串作为代码执行

# exec("sqrt = 1") # !!!需要指定命名空间，否则代码将修改你的变量
# sqrt(4)
scope = {} # 字典用作代码字符串的命名空间
exec("sqrt = 1", scope)
print(sqrt(4))
# print(scope)
print(scope['sqrt'])

# eval类似exec, 计算用字符串表示的python表达式的值
sting = "6 + 18 * 2"
print(eval(sting))


