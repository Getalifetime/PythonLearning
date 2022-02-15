#函数

def greet_user(username):
    print("Hello, " + username.title() + "!")

def favourite_book(bookname):
    print("One of my favourite book is 《" + bookname + '》.')
    
greet_user('alex')
favourite_book('Alice in Wonderland')

x = greet_user('alex')
print("所有的函数都有返回值，如果没告诉他们返回什么则返回None")
print(x)    #由此可知，所有的函数都有返回值，如果没告诉他们返回什么则返回None

#位置实参和关键字实参
def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type + ", It's name is " + pet_name.title() + ".")

#位置实参
describe_pet('cat', 'tom')

# 关键字实参
# 关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。
# 对于函数调用中的关键字实参，等号两边不要有空格
describe_pet(pet_name='harry', animal_type="dog")

#默认值
# 编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；否则，将使用形参的默认值。这种方式也可将实参变成可选的
# 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。
# 给形参指定默认值时，等号两边不要有空格
def describe_pet_d(pet_name, animal_type="dog"):
    print("I have a " + animal_type + ". It's name is " + pet_name.title() + ".")

describe_pet_d(pet_name = 'jack')
describe_pet_d('jack')
describe_pet_d('jack','hamster')

#可选实参
#可给实参指定一个默认值——空字符串，让其变成可选的
def describe_pet_s(pet_name, animal_type, pet_gender=''):
    if pet_gender:
        print("I have a " + animal_type + ". It's name is " + pet_name.title() + ". And it's" + pet_gender.title())
    else :
        print("I have a " + animal_type + ". It's name is " + pet_name.title() + ".")

describe_pet_s('harry', 'dog')
describe_pet_s('harry', 'dog', 'male')


#返回值
def cube_value(number):
    value = number**3
    return value
    
value = cube_value(3)
print("\nThe return value is " + str(value) + ".")

#传递列表
print('\n传递列表')

def greet_users(usernames):
    for name in usernames:
        msg = "Hello, " + name + "!"
        print(msg)
        
usernames = ['John', 'TK', 'Alex', 'Aqi']
greet_users(usernames)

#在函数中修改列表
print('\n在函数中修改列表：')

def print_models(unprinted_designs, completed_models):
    """打印列表unprinted_3Ddesigns中每个设计，并在打印完成后将其移到已完成列表completed_models"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '显示打印好的所有模型'
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print('- ' + completed_model)
        
unprinted_3D_designs = ['Phone case', 'dodecahedron', 'robot']
completed_models = []
print_models(unprinted_3D_designs[:], completed_models) #传递列表的副本以防止修改原始列表
show_completed_models(completed_models)

'''
这个程序还演示了这样一种理念，即每个函数都应只负责一项具体的工作。第一个函数打印每个设计，而第二个显示打印好的模型；这优于使用一个函数来完成两项工作。
编写函数时，如果你发现它执行的任务太多，请尝试将这些代码划分到两个函数中。
别忘了，总是可以在一个函数中调用另一个函数，这有助于将复杂的任务划分成一系列的步骤。
'''

print("\n函数实参传递的是列表的副本(完整切片)，所以原列表内容不变:")
print(unprinted_3D_designs)
"""
 虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，
 因为让函数使用现成列表可避免花时间和内存创建副本，从而提高效率，在处理大型列表时尤其如此。
"""

 
# 传递任意数量的实参
print("\n传递任意数量的实参")
### 星号*让Python创建一个空元组，并将收到的所有值都封装到这个元组中
def favourite_cars(*cars):
    print("I like these cars:")
    for car in cars:
        print('- ' + car)
    
favourite_cars('C-HR', 'HighLander', 'Camry', 'Corolla')        
        
        
# 结合使用位置实参和任意数量实参
### 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
### Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(12, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')   
        
# 使用任意数量的关键字实参
## 有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键—值对
## 形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所名称—值对都封装到这个字典中。
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             feild='physics')
print(user_profile)

def make_car(manufacturer, model, **extra_info):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for key,value in extra_info.items():
        car_info[key] = value
    return car_info
car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

#给函数编写文档
def square(x):
    'Calculates the square of the number x.'    #文档字符串，作用是给函数注释，将作为函数的一部分存储起来
    return x**2
print(square.__doc__)   #__doc__是函数的一个属性，属性名中的双下划线表示这是一个特殊的属性
help(square)    #在交互式解释器中，可使用特殊的内置函数help获取有关函数的信息，其中包含函数的文档字符串
    
    
        






      