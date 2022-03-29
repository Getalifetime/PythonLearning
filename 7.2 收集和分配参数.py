"""
允许可变数量的参数
"""
#1 参数前面的*将提供的所有的值都放在一个元组中，也就是将这些值收集起来
def print_params(*params):
    print(params)

print_params('Testing')
print_params(1, 2, 3)
print_params() # 没有提供可供收集的参数，输出将是一个空元组

#2 *意味着收集余下位置的参数
def print_params_2(title, *params):
    print(title)
    print(params)

print_params_2('Params:', 1, 2, 3)
print_params_2('Nothing:')
#print_params_2('Hmm...', something=42) # *不会收集关键字参数

#3 此情况下需要使用名称来指定后续参数
def in_the_middle(x, *y, z):
    print(x, y, z)

in_the_middle(1, 2, 3, 4, 5, z=7) 

#4 **可收集关键字参数
def print_params_3(**params):
    print(params)

print_params_3(x=1, y=2, z=3) # 结果得到一个字典

#5 结合使用以上内容
def print_params_4(x, y, z=3, *pospar, **keypar):
    print(x, y, z)
    print(pospar)
    print(keypar)

print_params_4(1, 2, 4, 7, 8, 9, foo=1, bar=2)

#6 分配参数
def add(x, y): # 模块operator提供了add函数的高效版本
    return x + y

params = (1, 2)
result = add(*params) # 在调用函数时使用运算符*来分配参数
print(result)

#7 将字典中的值分配给关键字参数
def hello_to_someone(greeting='Hello', name='world'):
    print('{}, {}!'.format(greeting, name))

params = {
    'name': 'Sir Robin',
    'greeting': 'Well met',
}
hello_to_someone(**params)

### 只有在定义函数或调用函数时，星号才能发挥作用
### 如果在定义和调用函数时都使用了*或**，结果与不使用*或**一样，因此这种情况下还不如不使用它们


#8 使用拆分运算符来传递参数，无需操心参数个数之类的问题。在调用父类的构造函数时特别有用
def foo(x, y, z, m=0, n=0):
    print(x, y, z, m, n)

def call_foo(*args, **kwds):
    print("Calling foo!")
    foo(*args, **kwds)

call_foo(1, 1, 0, 1, 1)
