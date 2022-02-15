from cmath import pi
from string import capwords
import cmath


"""
 对字符串调用方法format，并提供要设置其格式的值
 每个值都被插入字符串中，以替换用花括号括起来的替换字段

"""
# 替换字段名
# 按顺序将字段和参数进行匹配，也可给参数指定名称，也可将两种方式混合使用
print( "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3) )
# 通过索引指定要在哪个字段中使用相应的未命名参数，这样就可不按顺序
# 但不能同时使用手动编号和自动编号，这样很快会变得混乱不堪
print( "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3) )

fullname = ['ALex', 'Liu']
print( "Mr {name[1]}".format(name=fullname))

tmpl = "The {mod.__name__} module defines the value of pi: {mod.pi}"
print( tmpl.format(mod=cmath) )

# 设置转换标志 !r(表示repr) !s(表示str) !a(表示ascii)
print( "{pi!r} {pi!s} {pi!a}".format(pi="π") ) # 函数repr尝试创建给定值的Python表示

# 指定要转换值的类型
print( "The number is {num}".format(num=42) )
print( "The number is {num:f}".format(num=4.2) ) # f 将小数表示为定点数，默认显示6位小数
print( "The number is {num:b}".format(num=42) )  # b 将整数表示为二进制数
print( "The number is {num:o}".format(num=42) )  # 0 将整数表示为八进制数
print( "The number is {num:x}".format(num=42) )  # x 将整数表示为十六进制数，字母小写
print( "The number is {num:X}".format(num=42) )  # X 将整数表示为十六进制数，字母大写
print( "The number is {num:%}".format(num=0.2) ) # % 将数表示为百分比值，按f设置格式

# 指定宽度
print( "{num:10}".format(num=3) )
print( "{name:10}".format(name="Bob") ) # 注意数字和字符串对齐方式不同

# 指定精度
print( "{pi:10.2f}".format(pi=pi) )

# 使用逗号来添加千位分隔符
print( "One googol is {:,}".format(10**100) )

# 在指定宽度和精度的数前面，可添加一个标志，可以是0，+，-，或空格
print( "{:010.2f}".format(pi) )

# 要指定左对齐、右对齐和居中，可分别使用<, >, ^
print( "{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}".format(pi) )
# 可以用指定字符来扩充对齐说明符
print( "{:$^20}".format(" WIN BIG "))
# 说明符= 指定将填充字符放在符号和数字之间
print( "{0:10.2f}\n{1:=10.2f}".format(pi, -pi) )
# 给正数加符号，使用说明符+
print( "{0:+.2}\n{1:.2}".format(pi, -pi) )
# 空格说明符会在正数前面加上空格
print( "{0: .2}\n{1: .2}".format(pi, -pi) )
# 井号#放在符号说明符和宽度之间将对结果加上一个前缀
print( "{:#b}".format(42) )
print( "{:#o}".format(42) )
print( "{:#x}".format(42) )
# #g保留十进制数的小数点
print( "{:#g}".format(42) )

#例子：根据指定的宽度打印格式良好的价格列表
width = 35

price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt        = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

# 打印表头
print('=' * width)
print(header_fmt.format('Item','Price'))
print('-' * width)

# 打印价格列表
print(fmt.format('Apple', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))

#打印表尾
print('=' * width)

"""
字符串方法
"""
# 方法center将字符串居中并在两边添加填充字符（默认空格）
print( "center".center(30) )
print( "center".center(30, "*") )

# 在字符串中查找子串，若找到则返回子串第一个字符的索引，否则返回-1
sentence = "With a moo-moo here, and a moo-moo there"
print( sentence.find("moo") )
print( sentence.find("mooo") )
print( sentence.find("moo", 10)) #只指定搜索的起点
print( sentence.find("moo", 15, 33)) #指定搜索的起点和终点(搜索范围包含起点的值但不包含终点的值)

# 查找总共出现的次数，并标记位置
totle = 0
start = 0
pos = []

while 1:
    result = sentence.find("moo", start)
    if result != -1:
        totle += 1
        start = result + 3
        pos.append(result)
    else:
        break
print("totally found times: {}".format(totle))
print("positions: {}".format(pos))

# 方法join用于合并序列的元素，所合并序列的元素必须都是字符串
seq = ['1', '2', '3', '4', '5']
sep = "+"
seq_merge = sep.join(seq)
print(seq_merge)

dirs = '', 'usr', 'bin', 'env'
print(dirs)
print('\\'.join(dirs))

# 大小写
sentence = "that's all, folks"
print(sentence.title())  # title方法确定边界的方式可能导致结果不合理
print(capwords(sentence)) # 另一种方法是使用模块string中的函数capwords

# 方法replace将指定子串替换为另一个字符串
sentence = "This is a test"
print(sentence.replace('is', 'ezz'))

# 方法split作用与join相反
print(seq_merge.split('+'))
print("Use the Force".split()) #没有指定分隔符时，将默认在单个或多个连续的空白字符（空格、制表符、换行符等）进行拆分

# 方法strip将字符串开头和末尾的空白删除，还可指定要删除哪些字符
sentence = "*** SPAM * for * everyone!! ***"
print(sentence.strip('* !'))