import unittest

from function import get_formatted_name
from _8_1ClassCar import Car

"""
Python标准库中的模块unittest提供了代码测试工具。
单元测试        用于核实函数的某个方面没有问题；
测试用例        是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
               良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。
全覆盖式测试用例 包含一整套单元测试，涵盖了各种可能的函数使用方式。
                对于大型项目，要实现全覆盖可能很难。
                通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。
"""

class NamesTestCase(unittest.TestCase):
    '测试get_formatted_name函数功能'
    def test_first_last_name(self):
        formatted_name = get_formatted_name('charlie', 'chaplin')
        self.assertEqual(formatted_name, 'Charlie Chaplin')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

#unittest.main() #代码行unittest.main()让Python运行这个文件中的测试，，所有以test_打头的方法都将自动运行

""" 
        unittest Module中的断言方法
    方 法                       用 途
    assertEqual(a, b)           核实a == b
    assertNotEqual(a, b)        核实a != b
    assertTrue(x)               核实x为True
    assertFalse(x)              核实x为False
    assertIn(item, list)        核实item在list中
    assertNotIn(item, list)     核实item不在list中
"""

class TestCar(unittest.TestCase):
    '针对Car类的测试'
    def setUp(self): 
        # Python将先运行方法setUp()，再运行各个以test_打头的方法。
        # 这样，在编写的每个测试方法中都可使用在方法setUp()中创建的对象了
        self.my_new_car = Car('bmw', 'the 5', '2018')
        self.descriptive_name = '2018 BMW The 5'
    def test_get_descriptive_name(self):
        self.assertEqual(self.descriptive_name, self.my_new_car.get_descriptive_name())
    def test_update_odometer(self):
        updated_odometer = 10000
        self.my_new_car.update_odometer(updated_odometer)
        self.assertEqual(updated_odometer, self.my_new_car.read_odometer())

unittest.main() #代码行unittest.main()让Python运行这个文件中的测试，，所有以test_打头的方法都将自动运行