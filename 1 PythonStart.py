from math import sqrt
from tkinter import Y

########################################################################################################
print("Hello Python interpreter")
print('先编写行之有效的代码，再决定是对其做进一步改进，还是转而去编写新代码')
#
print('\n\t****************字符串****************')
print("Hello Python!")
print('字符串引号可以是‘单引号’，也可以是“双引号”')
message = "Hello World!"
print(message)
print('这种灵活性能让你在字符串中包含引号和撇号')
print('He said, "Python is my favourite language".')
print("'Python' is named after Monty Python, not the snake")
# 

#
print('\n\t****************修改字符串大小写****************')
message = "alex liu"
print(message.title())
print(message.upper())
print(message.lower())
#存储数据时，方法lower() 很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储它们。
#以后需要显示这些信息时，再将其转换为最合适的大小写方式。
#
print('\n\t****************拼接字符串，使用加号“+”****************')
first_name = "alex"
last_name = "liu"
full_name = first_name + ' ' + last_name
msg = "Hello " + full_name.title() + '!'
print(msg)

print('\n\t****************使用制表符和换行符****************')
print("Language:\n\tPython\n\tC\n\tJavaScript")

print('\n\t****************删除空白****************')
message = " Hello Python "
print(message.lstrip())
print(message.rstrip())
print(message.strip())
message = message.strip()
print(message)

print("\n\t****************字符串长度****************")
string = "Have a good day!"
print('The length of "%s" is %d.' %(string, len(string)))

print('\n\t****************数字****************')
"""
######数字######
"""
a = 3
b = 2 
print("a/b =",a/b)
print("a//b =",a//b)
print("\t格式化输出:")
print("\ta/b = %f" %(a/b))
print("\ta//b = %d" %(a//b))
print("square a = ",a**2)
print("cube a = ",a**3)
print("cube a = ", pow(a,3)) # 乘方函数pow
print(10**6)
print("sqrt a = ", sqrt(a)) # 计算平方根





###浮点数
#Python将带小数点的数字都称为浮点数。从很大程度上说，使用浮点数时都无需考虑其行为。只需输入要使用的数字，Python通常都会按你期望的方式处理它们：
#但需要注意的是，结果包含的小数位数可能是不确定的.所有语言都存在这种问题，没有什么可担心的。
#Python会尽力找到一种方式，以尽可能精确地表示结果，但鉴于计算机内部表示数字的方式，这在有些情况下很难。就现在而言，暂时忽略多余的小数位数即可
print("0.2 * 2 = ",0.2 * 2)
print("0.2 + 0.1 = ",0.2 + 0.1)
print("0.2 * 0.1 = ",0.2 * 0.1)

#str()将非字符串值表示为字符串
age = 28
print("I'm " + str(age) + " years old!")

# 长字符串，使用三引号
print('''This is a very long stirng. It continues here.
And it's not over yet, "Hello, world!"
Still here.''')

# 原始字符串: 添加前缀r
print(r'C:\nowhere')

# 原始字符串不能以单个反斜杠结尾
# print("This is illegal\")
# print(r"This is illegal\")
# 解决此问题的基本技巧是将反斜杠单独作为一个字符串
print(r'C:\Program Files\foo\bar' '\\')

# 字符串就是由字符组成的序列
# Python没有专门用于表示字符的类型，因此一个字符就是只包含一个元素的字符串
greeting = 'Hello'
print(greeting[0])
print(greeting[-1])

# 使用del删除：不仅会删除对象引用，还会删除名称本身
x = ['Hello', 'world']
y = x
y[1] = 'python'
print(x)
del x
print(y) # 删除x对y没有任何影响，只是删除名称x





































