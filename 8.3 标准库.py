from collections import OrderedDict

"""
字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序。
要创建字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类。
OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。
"""
favourite_languages1 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', 
    'alice': 'go', 
    'bob': 'c++'# 在最后一个键—值对后面也加上逗号，为以后在下一行添加键—值对做好准备。
    }

favourite_languages2 = OrderedDict()
favourite_languages2['jen'] = 'python'
favourite_languages2['sarah'] = 'c'
favourite_languages2['edward'] = 'ruby'
favourite_languages2['phil'] = 'python'
favourite_languages2['Alice'] = 'go'

print("\nfavourite_languages1: ")
for name,language in favourite_languages1.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')

print("\nfavourite_languages2: ")
for name,language in favourite_languages2.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')