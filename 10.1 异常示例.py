"""
每当发生让Python不知所措的错误时，它都会创建一个异常对象。
如果你编写了处理该异常的代码，程序将继续运行；
如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。
异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办
"""
# 如何检查一个值能否用于除法运算呢，方法有很多，但最佳方法无疑是尝试将两个值相除，看是否可行
# 异常处理并不会导致代码混乱，而添加大量if语句来检查各种可能的错误状态将导致代码的可读性极差
print("Give me two numbers, and I'll divide them.") 
print("Enter 'q' to quit.") 
while True: 
    first_number = input("\nFirst number: ") 
    if first_number == 'q': 
        break 
    second_number = input("Second number: ") 
    try: 
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("** You can't devide by ZERO!")
    except ValueError:
        print("** Wrong type!")
    else: # 在try代码块成功执行时才需要运行的代码应放在else代码块中
        print(answer)
        break

# 要使用一个except语句捕获多种异常，可在一个元组中指定这些异常
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x / y)
# except (ZeroDivisionError, TypeError, NameError, ValueError):
#     print("Your numbers are bogus...")
except (ZeroDivisionError, TypeError, NameError, ValueError) as e:
    # 显式的捕获异常对象本身，让用户知道发生了什么情况
    print(e)

# 改进
while True:
    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print(x / y)
    except Exception as e:
        # 注意为数不多的异常如SystemExit和KeyboardInterrupt是从BaseException（Exception的父类）派生而来的
        # 因此这些将成为漏网之鱼
        print(e)
    else:
        # 万事大吉时跳出循环
        break

# 处理文件找不到的异常
filename = 'alice.txt' 
try: 
    with open(filename) as f_obj: 
        contents = f_obj.read() 
except FileNotFoundError: 
    msg = "Sorry, the file " + filename + " does not exist." 
    print(msg) 

# 例：
def count_words(filename):
    '计算文档的字数'
    try: 
        with open(filename) as f_obj: 
            contents = f_obj.read() 
    except FileNotFoundError: 
        pass #失败时一声不吭
    else:
        words = contents.split()
        words_num = len(words)
        print('The file "' + filename + '" has about ' + str(words_num) + " words.") 

filenames = ['test article.txt', 'article1.txt', 'article2.txt']
for filename in filenames:
    count_words(filename)