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
age = 32
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
elif age >= 4 and age < 18:
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

