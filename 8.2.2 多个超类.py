from subprocess import call


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
    
class Talker:
    def talk(self):
        print("Hi, my value is", self.value)

class TalkingCalculator(Calculator, Talker):
    pass

print(TalkingCalculator.__bases__)

tc = TalkingCalculator()
tc.calculate("1 + 2 * 3")
tc.talk()


# 除非万不得已，应避免使用多重继承，因为有些情况下它可能带来意外的并发症
# 若多个超类以不同的方式实现了同一个方法，必须在class定义中小心排列这些超类，
# 位于前面位置的类的方法将会覆盖后面的类的方法

### 接口和内省
# 一般而言，无需过于深入研究对象，而只依赖多态来调用所需的方法
# 接口——对外暴露的方法和属性。
# python不显式编写接口，而是假定对象能完成你要求它完成的任务。若不能完成，程序将失败
# 然而，不是直接调用方法并期待一切顺利，而是检查所需的方法是否存在
print(hasattr(tc, 'talk'))
print(hasattr(tc, 'fnord'))

# 检查属性是否可以调用
# getaddr可指定属性不存在时使用的默认值，这里指定为None
print(callable(getattr(tc, 'talk', None)))
print(callable(getattr(tc, 'fnord', None)))

# 设置对象的属性
setattr(tc, 'name', 'Arnold')
print(tc.name)

# 检查对象中存储的所有值
print(tc.__dict__)

# 要确定对象由什么组成，可使用模块inspect，该模块让用户能够以图形方式浏览python对象