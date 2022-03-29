# 对象可能隐藏（封装）其内部状态。在有些语言中（如Java），意味着对象的状态（属性）只能通过其方法来访问
# 在Python中，所有的属性都是公有的。但直接访问对象状态时应谨慎行事，因为可能在不经意间导致状态不一致

# python没有为私有属性提供直接的支持，通过玩点小花招可获得类似于私有属性的效果
# 在方法或属性的名称前以两个下划线开头即可

class Secretive:

    def __inaccessible(self):
        print("you can't see me ...")
    
    def accessible(self):
        print("The secret message is :")
        self.__inaccessible()
    
s = Secretive()
# s.__inaccessible() # 从外部不能直接访问__inaccessible，但在类中可以使用它
s.accessible()

# 然而python这种处理手法并不标准：在类定义中，对所有的以两下划线开头的名称都进行转换，即在开头加上一个下划线和类名
s._Secretive__inaccessible() # 照样可以执行

# 总之python无法禁止别人访问对象的私有化方法和属性
# 但上面的修改方式发出了强烈的信号，让别人不要试图修改
# from module import * 不会导入以下划线打头的名称

