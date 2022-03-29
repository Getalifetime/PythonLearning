#1 通过存取方法定义的属性通常称为特性(Property)

class Rectangle1:
    def __init__(self):
        self.width = 0
        self.height = 0
    
    def set_size(self, size):
        self.width, self.height = size
    
    def get_size(self):
        return self.width, self.height

    # 函数property将存取方法作为参数创建一个特性，将名称size关联到这个特性
    size = property(get_size, set_size) # 注意：获取方法在前，存取方法在后

r = Rectangle1()
r.width = 10
r.height = 5
print(r.size)
r.size = 150, 100
print(r.width)
# 属性size依然受制于get_size和set_size执行的计算，但看起来就像普通属性一样

# properity实际是一个类，共有4个参数
#  如果没有指定任何参数，创建的特性将既不能读也不可写
#  如果只指定一个参数（获取方法），创建的特性将是只读的
#  第三个参数是可选的，指定用于删除属性的方法
#  第四个参数也是可选的，指定一个文档字符串，分别名为fget、fset、fdel和doc。若要创建一个只可写且带文档字符串的特性，可使用它们作为关键字参数来实现
 

#2 静态方法和类方法
# 静态方法和类方法是这样创建的：将它们分别包装在staticmethod和classmethod类的对象中。
# 静态方法的定义中没有参数self，可直接通过类来调用。
# 类方法定义中包含类似self的参数，通常被命名为cls。类方法也可通过对象直接调用，参数cls直接关联到类
class MyClass1:
    def smeth():
        print("This is a static method")
    # 手工包装和替换方法
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print("This is a class method of", cls)
    cmeth = classmethod(cmeth)

class MyClass2:
    '使用装饰器来包装方法，Python 2.4引入'
    @staticmethod
    def smeth():
        print("This is a static method")

    @classmethod
    def cmeth(cls):
        print("This is a class method of", cls)

MyClass1.smeth()
MyClass2.cmeth()

#3 __getattr__, __setattr__等方法。可以在这些方法中编写处理多个特性的代码。然而，在可能的情况下
#  还是使用函数property吧
# __getattribute__(self, name): 在属性被访问时自动调用，只适用于新式类
# __getattr__(self, name): 在属性被访问而对象没有这样的属性时自动调用
# __setattr__(self, name, value): 试图给属性赋值时自动调用
# __delattr__(self, name): 试图删除属性时自动调用 
class Rectangle2:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:                           
            # __dict__属性是一个字典，其中包含所有的实例属性
            # 之所以使用它而不是执行常规属性赋值，是要避免再次调用__setattr__进而导致无限循环
            self.__dict__[name] = value 
    def __getattr__(self, name):    
        # 仅当没有找到指定的属性时才会调用。这意味着如果指定的名称不是size，将引发AttributeError异常
        # 这在要让类能够正确的支持hasattr和getattr等内置函数时很重要
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

r = Rectangle2()
r.width = 8
r.height = 3
print(r.size)
r.size = 88, 33
print(r.width)