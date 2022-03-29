#继承

from _8_1ClassCar import Car

class Battery():
    '模拟电动汽车的电池'
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        '打印一条描述电池容量的信息'
        print("This car has a "+ str(self.battery_size) + "-KWh battery.")

    def get_range(self): 
        """打印一条消息，指出电瓶的续航里程""" 
        if self.battery_size == 70: 
            range = 240 
        elif self.battery_size == 85: 
            range = 270 
 
        message = "This car can go approximately " + str(range) 
        message += " miles on a full charge." 
        print(message)

class ElectricCar(Car):
    '模拟电动汽车的独特之处'
    def __init__(self, make, model, year):
        '初始化父类的属性，再初始化子类独有的属性'
        super().__init__(make, model, year)
        self.battery = Battery() #将一个Battery实例用作ElectricCar类的一个属性
        # 实际上，函数super返回的是一个super对象，这个对象负责为你执行方法解析。
        # 当访问它的属性时，它将在所有的超类（以及超类的超类等等）中查找，直到找到指定的属性或引发AttributeError异常
        """
        使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。
        在这种情况下，可能需要将类的一部分作为一个独立的类提取出来。
        你可以将大型类拆分成多个协同工作的小类。
        """

    def fill_gas_tank(self): # 重写父类的方法
        print("This car doesn't need a gas tank!")
            

if __name__ == "__main__":        
    #help(Car)
    #print(Car.__doc__)  #打印文档字符串
    my_tesla = ElectricCar('tesla', 'model s', 2018)
    print(my_tesla.get_descriptive_name())

    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()

    my_tesla.battery.battery_size = 85
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()

    my_tesla.fill_gas_tank()


# 一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的模块中。
# 如果你喜欢模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。
# 先找出让你能够编写出可行代码的方式，再尝试让代码更为组织有序。