import random
from wsgiref.util import guess_scheme   #随机数模块

cheatMode = True

basicNum = 100
answer = random.randint(1, basicNum)   # ?-?的整数

if cheatMode:
    print("answer = " + str(answer))

print("\nGuess my number..range from 1 to " + str(basicNum))
guess_round = 0
guess_times = 0
guessed_numbers = []
total_statistics = {}
active = True

while active:
    
    #函数input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便后续使用。
    if guess_times == 0:
        sinput1 = input("\nPlease input your answer: ")
    else:
        sinput1 = input("\nNow please retry: ")
   
    if sinput1.isdigit():
        print("\nYour number is " + sinput1)
    else:
        print("\nPlease input a digital, try again.")
        continue
    '''
    #用isdigit函数判断字符串是否为全数字
    #用isalpha函数判断字符串是否为全字母
    #用isalnum函数判断字符串是否字母和数字的组合
    if sinput1.isalpha():
        print("全字母")
    elif sinput1.isalnum():
        print("数字+字母")
    '''
    number = int(sinput1) #函数int()将数字的字符串表示转换为数值表示
    guessed_numbers.append(number)

    if number == answer:
        print("Congratulations，your answer is right!")
        print("You tried " + str(guess_times) + " times. And this is your guessed numbers:")
        print(guessed_numbers)
        total_statistics[guess_round] = guessed_numbers
        sinput2 = input("\nPlay again? Y/N ")
        while 1:            
            if sinput2 == 'N' or sinput2 == 'Y' or sinput2 == 'n' or sinput2 == 'y' or sinput2 == '':#回车键
                guess_times = 0
                break
            else:
                sinput2 = input("\nPlease input Y or N: ")
                continue
        
        if sinput2 == 'Y' or sinput2 == 'y' or sinput2 == '':
            guess_round += 1
            guessed_numbers = []

            basicNum = basicNum * 10
            print("\nWe will improve the difficulty this time. (1, %d)" %basicNum)
            answer = random.randint(1, basicNum)
            if cheatMode:
                print("answer = " + str(answer))
            continue
        else:
            active = False
            print("Your statistic data:")
            for round, numbers in total_statistics.items():
                print(" Round " + str(round + 1))
                print("\tGuessed numbers: " + str(numbers))
            print("\nSee you next time. Bye!")
            #break
    elif number < answer:
        guess_times += 1
        print("Wrong! The answer is a larger number")
    else:
        guess_times += 1
        print("Wrong! The answer is a lower number")
        
'''
使用input和raw_input都可以读取控制台的输入，但是input和raw_input在处理数字时是有区别的
纯数字输入

当输入为纯数字时

    input返回的是数值类型，如int,float
    raw_inpout返回的是字符串类型，string类型

输入字符串为表达式

input会计算在字符串中的数字表达式，而raw_input不会。

如输入 “57 + 3”:

    input会得到整数60
    raw_input会得到字符串”57 + 3”
'''

"""
import random
print(random.random())      #随机大于0 且小于1 之间的小数
print(random.uniform(0,9))  #随机一个大于0小于9的小数
print(random.randint(1,5))  #随机一个大于等于1且小于等于5的整数
print(random.randrange(1,10,2))   #随机一个大于等于1且小于等于10之间的奇数，其中2表示递增基数
print(random.choice(['123','abc',52,[1,2]]))    #随机返回参数列表中任意一个元素
print(random.sample(['123','abc',52,[1,2]],2))  #随机返回参数列表中任意两个元素，参数二指定返回的数量
lis = [1,2,5,7,9,10]
random.shuffle(lis) #打乱列表顺序
print(lis)
"""