"""
#####元组#####
"""
# 列表非常适合用于存储在程序运行期间可能变化的数据集。
# 列表是可以修改的，然而有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。
# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。
# 元组看起来犹如列表，但使用圆括号而不是方括号来标识
aTuple = (123, 'Google', 'JD', 'Taobao')
print(aTuple)
print("遍历元组：")
for val in aTuple:
	print("\t",val)
#aTuple.append('456')
#aTuple[0]=456

print ("\n将元组转化为列表：\n转换前：", aTuple)
alist = list(aTuple)
print ("转换后：", alist)
alist.append('456')
print('末尾追加元素：',alist)

# 函数tuple将序列转换为元组
print('\n将序列转换为元组')
a = [1, 2, 3]
print(tuple(a))
b = "Hello"
print(tuple(b))

# 一个值的元组，必须在元素后面加上逗号
print("\n一个值的元组")
print( 3*(40) )
print( 3*(40,) )

# 元组的切片还是元组
print("\n元组的切片")
print( aTuple[0:2] )

# 自己编写程序时，几乎所有的情况下都可以使用列表代替元组，
# 一种例外情况: 将元组用作字典键，而列表不行，因为字典键是不允许修改的

'''
4.6.1　格式设置指南
若要提出Python语言修改建议，需要编写Python改进提案 （Python Enhancement Proposal，PEP）。PEP 8是最古老的PEP之一，它向Python程序员提供了代码格式设置指南。PEP 8的
篇幅很长，但大都与复杂的编码结构相关。
Python格式设置指南的编写者深知，代码被阅读的次数比编写的次数多。代码编写出来后，调试时你需要阅读它；给程序添加新功能时，需要花很长的时间阅读代码；与其他程序
员分享代码时，这些程序员也将阅读它们。
如果一定要在让代码易于编写和易于阅读之间做出选择，Python程序员几乎总是会选择后者。下面的指南可帮助你从一开始就编写出清晰的代码。
4.6.2　缩进
PEP 8建议每级缩进都使用四个空格，这既可提高可读性，又留下了足够的多级缩进空间。
在字处理文档中，大家常常使用制表符而不是空格来缩进。对于字处理文档来说，这样做的效果很好，但混合使用制表符和空格会让Python解释器感到迷惑。每款文本编辑器都提
供了一种设置，可将输入的制表符转换为指定数量的空格。你在编写代码时应该使用制表符键，但一定要对编辑器进行设置，使其在文档中插入空格而不是制表符。
在程序中混合使用制表符和空格可能导致极难解决的问题。如果你混合使用了制表符和空格，可将文件中所有的制表符转换为空格，大多数编辑器都提供了这样的功能。
4.6.3　行长
很多Python程序员都建议每行不超过80字符。最初制定这样的指南时，在大多数计算机中，终端窗口每行只能容纳79字符；当前，计算机屏幕每行可容纳的字符数多得多，为何还
要使用79字符的标准行长呢？这里有别的原因。专业程序员通常会在同一个屏幕上打开多个文件，使用标准行长可以让他们在屏幕上并排打开两三个文件时能同时看到各个文件
的完整行。PEP 8还建议注释的行长都不超过72字符，因为有些工具为大型项目自动生成文档时，会在每行注释开头添加格式化字符。
PEP 8中有关行长的指南并非不可逾越的红线，有些小组将最大行长设置为99字符。在学习期间，你不用过多地考虑代码的行长，但别忘了，协作编写程序时，大家几乎都遵守
PEP 8指南。在大多数编辑器中，都可设置一个视觉标志——通常是一条竖线，让你知道不能越过的界线在什么地方。
注意 　附录B介绍了如何配置文本编辑器，以使其：在你按制表符键时插入四个空格；显示一条垂直参考线，帮助你遵守行长不能超过79字符的约定。
4.6.4　空行
要将程序的不同部分分开，可使用空行。你应该使用空行来组织程序文件，但也不能滥用；只要按本书的示例展示的那样做，就能掌握其中的平衡。例如，如果你有5行创建列表
的代码，还有3行处理该列表的代码，那么用一个空行将这两部分隔开是合适的。然而，你不应使用三四个空行将它们隔开。
空行不会影响代码的运行，但会影响代码的可读性。Python解释器根据水平缩进情况来解读代码，但不关心垂直间距。
4.6.5　其他格式设置指南
PEP 8还有很多其他的格式设置建议，但这些指南针对的程序大都比目前为止本书提到的程序复杂。等介绍更复杂的Python结构时，我们再来分享相关的PEP 8指南。
'''
