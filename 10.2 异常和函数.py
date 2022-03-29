"""
异常和函数有着天然的联系
如果不处理函数中引发的异常，它将向上传播到调用函数的地方
如果在那里也未得到处理，异常将继续传播，知道到达主程序（全局作用域）。
如果主程序中也没有异常处理程序，程序将终止并显示栈跟踪消息
"""
def faulty():
    raise Exception("something is wrong")

def ignore_exception():
    faulty()

def handle_exception():
    try:
        faulty()
    except:
        print('exception handled')

ignore_exception()
# handle_exception()