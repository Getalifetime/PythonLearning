"""
所有的import 语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。
"""

#将函数存储在模块中

'''1.导入整个模块'''
#要让函数是可导入的，得先创建模块。模块 是扩展名为.py的文件，包含要导入到程序中的代码。
#import 函数.py

'''2.导入特定的函数'''
#可根据需要从模块中导入任意数量的函数
#from module_name import function_name
#from module_name import function_0, function_1, function_2
from function import greet_user
greet_user("alex")

#from 函数 import make_pizza
#make_pizza(16, 'pepperoni')

'''3.使用as给函数指定别名'''
# 如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名
from function import greet_user as gu
gu('alex')

'''4.使用as给模块指定别名'''
# 通过给模块指定简短的别名，让你能够更轻松地调用模块中的函数。
import function as f
f.greet_user('ls')

'''5.导入模块中的所有函数'''
from function import *
# 由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。
greet_user('mx')
# 然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法：
#   如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
#     Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数
# 最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。