import json
"""
模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，
被包括Python在内的众多语言采用
"""
# 存储数据
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
numbers1 = [2, 3, 5, 7, 11, 13] 
filename = 'numbers.json' 
with open(filename, 'w') as f_obj: 
    json.dump(numbers1, f_obj) #json.dump接受两个实参：要存储的数据以及可用于存储数据的文件对象
    #json.dump(people, f_obj)

# 读取数据
with open(filename, 'r') as f_obj: 
    numbers2 = json.load(f_obj) 
print(numbers2)
#这是一种在程序之间共享数据的简单方式

# 例：读取已设置的用户名，未设置则提示设置
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Please register your user name: ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("Thanks for registering")
else:
    print("Welcome back, " + username + "!")