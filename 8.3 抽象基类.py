from abc import ABC, abstractmethod
from calendar import c

# 很多其他语言（如Java和GO）都采用显式指定接口的理念，Python通过引入模块abc提供了官方解决方案。这个模块为所谓的抽象类提供了支持
# 一般而言，抽象类是不能实例化的类，其职责是定义子类应该实现的一组抽象化方法

class Talker(ABC):
    @abstractmethod # 将方法标记为抽象的。形如@this的东西被称为装饰器
    def talk(self):
        pass

class Knigget(Talker):    
    
    # 若没有重写方法talk，则这个类也是抽象的，不能实例化
    """
    def talk(self):
        pass
    """

    def talk(self):
        print("Ni!")

class Herring:
    def talk(self):
        print("Blub.")

class Clam:
    pass

k = Knigget()
k.talk()

# 我们不关心对象是什么，只关心对象能够做什么。只要实现了方法talk，依然能够通过类型检查
h = Herring()
print(isinstance(h, Talker))
# 这时可将Herring注册为Talker，这样所有的Herring对象都将视为Talker对象
Talker.register(Herring)
print(isinstance(h, Talker))
print(issubclass(Herring, Talker))
# 然而，这种做法存在一个缺点，就是直接从抽象类派生提供的保障没有了
Talker.register(Clam)
print('\n')
print(issubclass(Clam, Talker))
c = Clam()
print(isinstance(c, Talker))
c.talk() # 失败
# 应将isinstance返回True视为一种意图表达，在这里Clam有成为Talker的意图，相信它能承担Talker的职责，但可悲的是它失败了