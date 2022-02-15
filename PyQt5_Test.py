import sys
'''
###1
from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
'''

###2
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
widget = QWidget()
widget.resize(960, 640)
widget.move(200,200)
widget.setWindowTitle("Hello, PyQt5!")
widget.show()

sys.exit(app.exec_())

'''
上面的代码示例会在屏幕上显示一个小窗口。

import sys
from PyQt5.QtWidgets import QApplication, QWidget
这里我们进行了一些必要模块的导入。最基础的widget组件位于PyQt5.QtWidget模块中

app = QApplication(sys.argv) 
所有的PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。

w = QWidget()
Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。

w.resize(250, 150) 
resize()方法调整了widget组件的大小。它现在是250px宽，150px高。

w.move(300, 300)
move()方法移动widget组件到一个位置，这个位置是屏幕上x=300,y=300的坐标。

w.setWindowTitle('Simple')
这里我们设置了我们窗口的标题。这个标题显示在标题栏中。

w.show() 
show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。

sys.exit(app.exec_())
最后，应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，并且转发他们到widget应用上处理。
如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。
exec_()方法有一个下划线。因为exec是Python保留关键字。因此，用exec_()来代替。
'''