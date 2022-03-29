###字典###
'''
# 在Python中，字典是一系列的“键——值”对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值
# 与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
# 字典用放在花括号{} 中的一系列键—值对表示
'''

print('\n访问字典中的值')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print('\n添加“键——值”对')
print(alien_0)
alien_0['x_position'] = 5
alien_0['y_position'] = 25
print(alien_0)

print('\n修改“键——值”对')
alien_0['x_position'] = 10
print(alien_0)

print('\n删除“键——值”对。使用del 语句时，必须指定字典名和要删除的键。')
del alien_0['points']
print(alien_0)

print('\n创建一个空字典')
alien_1 = {}
print('alien_1: ', alien_1)

print('\n字典拷贝')
print('未拷贝副本:')
alien_1 = alien_0
alien_0['points'] = 5
print('alien_0: ', alien_0)
print('alien_1: ', alien_1)

print('浅拷贝:')
alien_2 = alien_0.copy()
alien_0['x_position'] = 30
alien_0['y_position'] = 30
alien_2['color'] = 'yellow'
print('alien_0: ', alien_0)
print('alien_2: ', alien_2)

# 字典可存储一个对象的多种信息，也可以使用字典来存储众多对象的同一种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', # 在最后一个键—值对后面也加上逗号，为以后在下一行添加键—值对做好准备。
    }
print("\n phil's favorite language is " + favorite_languages['phil'].title())

print('\n###遍历字典：')
# 字典可用于以各种方式存储信息，因此有多种遍历字典的方式：可遍历字典的所有键—值对、键或值。

print('遍历所有的键——值对，使用方法items()')
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
    language.title() + ".")
# 注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系

print('\n只遍历所有的键，使用方法keys()')
i = 0
for name in favorite_languages.keys():
    i += 1
    print(str(i)+" name: ", name.title())
# 遍历字典时，会默认遍历所有的键。
# 因此，如果将上述代码中的for name in favorite_languages.keys(): 替换为for name in favorite_languages: ，输出将不变。

if 'eric' not in favorite_languages.keys():# 方法keys() 并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键
    print("Eric, please take our poll!")
    favorite_languages['eric'] = 'python'
    print(favorite_languages.keys()) 

# 字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。
# 要以特定的顺序返回元素，一种办法是在for 循环中对返回的键进行排序。
print('\n使用函数sorted() 来获得按特定顺序排列的键列表的副本：')
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

print('\n遍历字典中所有的值，使用方法values()')
for language in favorite_languages.values():
    print(language.title())

# 为剔除重复项，可使用集合（set）。集合类似于列表，但每个元素都必须是独一无二的：
print("\n剔除重复项：" + str(set(favorite_languages.values())))
for language in set(favorite_languages.values()):
    print(language.title())

'''
嵌套
'''
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
# 你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。
print("\n嵌套——可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典")
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

print("\nCreate 30 aliens")
aliens = []
for num in range(30):
    new_alien = alien_0.copy()
    new_alien['speed'] = 'low'
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print("Totle numbers of aliens: " + str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien["speed"] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien["speed"] = 'fast'
        alien['points'] = 15

print("\nNow some aliens changed:")
for alien in aliens[:5]:
    print(alien)
print("...")

print("\n在字典中存储列表")
favorite_languages = {
    'jen': ['python','c'],
    'sarah': 'c',
    'edward': ['ruby','go'],
    'phil': ['python', 'java'],
    }
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())

print("\n在字典中存储字典")
scientists = { 
    'aeinstein': { 
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton', 
        }, 
    'mcurie': {
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
        }, 
    } 

for name, info in scientists.items():
    print("\nScientist: " + name.title())
    full_name = info['first'] + ' ' + info['last']
    location = info['location']
    print("\tFullname: " + full_name.title())
    print("\tLocation: " + location.title())

# Python支持一种数据结构的基本概念，名为“容器”（container）
# 容器基本上就是可包含其他对象的对象
# 两种主要的容器是序列（如列表和元组）和映射（如字典）
# 在序列中，每个元素都有编号；在映射中，每个元素都有名称（也叫键）
# 有一种既不是序列也不是映射的容器，就是集合（set）

# 序列解包(或可迭代对象解包)
# 将一个序列(或任何可迭代对象)解包，并将得到的值存储到一系列变量中
# 这在使用元组(或其他序列或可迭代对象)的函数或方法时很有用
x, y, z = 1, 2, 3
x, y = y, x
print(x, y, z)

name, item = favorite_languages.popitem() # 将返回的元组解包到两个变量中
print(name, item)