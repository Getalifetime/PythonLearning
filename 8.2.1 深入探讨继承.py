# 多态：指的是能够同样的对待不同类型和类的对象，即无需知道对象属于哪个类就可以调用其方法


class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): 
    def init(self):
        self.blocked = ['SPAM']

seq = ['SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']
f = Filter()
f.init()
print(f.filter(seq)) # Filter类不会过滤任何信息

s = SPAMFilter()
s.init()
print(s.filter(seq))

# 内置方法issubclass 确定一个类是否为另一个类的子类
print(issubclass(SPAMFilter, Filter))
print(issubclass(Filter, SPAMFilter))

# 获取一个类的基类（父类），可访问其特殊属性__bases__
print(SPAMFilter.__bases__)
print(Filter.__bases__)

# isinstance 确定对象是否为特定类的实例
print(isinstance(s, SPAMFilter))
print(isinstance(s, Filter)) # s也是Filter的间接实例

print(isinstance(s, str)) # isinstance也可判断类型，如字符串类型str
print(isinstance('s', str))

# 获悉对象属于哪个类，可使用属性__class__
print(s.__class__)