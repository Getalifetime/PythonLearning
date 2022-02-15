#使用类和实例
class Car():
    '模拟汽车的类'
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #给属性指定默认值，此时无需包含为它提供初始值的形参
        
    def get_descriptive_name(self):
        '返回整洁的汽车描述信息'
        special_maker_list = ['bmw', 'vw']
        if str(self.make).lower() in  special_maker_list:
            make = str(self.make).upper()
        else:
            make = str(self.make)
        long_name = str(self.year) + ' ' + make + ' ' + str(self.model).title()
        return long_name
        
    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")
        return self.odometer
        
    def update_odometer(self, mileage):
        if(mileage >= self.odometer):
            self.odometer = mileage
        else:
            print("Warning: You can not roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer += miles

    def fill_gas_tank(self):
        print('Gas tank has been filled up.')


if __name__ == "__main__":      #此句的作用是该模块被import到其他模块时以下代码不会被执行
    my_new_car = Car('audi', 'a4 avant', '2019')
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

    #修改属性的值
    #1、直接修改属性的值
    my_new_car.odometer = 33
    my_new_car.read_odometer()

    #2、通过方法修改属性的值
    my_new_car.update_odometer(55)
    my_new_car.read_odometer()

    my_new_car.update_odometer(3)
    my_new_car.read_odometer()

    my_new_car.increment_odometer(11)
    my_new_car.read_odometer()

    my_used_car = Car('vw', 'sagitar', '2014')
    print('\nMy used car: ' + my_used_car.get_descriptive_name())
    my_used_car.update_odometer(39500)
    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()

