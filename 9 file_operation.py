# open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象；Python将这个对象存储在我们将在后面使用的变量中。
# 关键字with在不再需要访问文件后将其关闭
# 也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭

file_name = "learningsource\pi-30digits.txt"

with open(file_name) as file_object:
    content = file_object.read()
    print(content)

# 逐行读取
with open(file_name) as file_object:
    for line in file_object:
        print(line) # 每行末尾的换行符会单独打印，可用line.rstrip()去掉

# 创建一个包含文件各行内容的列表
with open(file_name) as file_object:
    lines = file_object.readlines()
print(lines)
# 使用文件的内容
pi_string = '' #读取文本文件时，Python将其中的所有文本都解读为字符串
for line in lines:
    pi_string += line.rstrip()
print(pi_string)

file_name = "learningsource\pi-million.txt"
with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string[:102] + "...") #打印小数点后100位

# 查找生日
birthday = "063090"
pos = pi_string.find(birthday)
if pos == -1:
    print("Your birthday does not appear in the first million digits of pi.")
else:
    print("Your birthday appears in the first million digits of pi!") 
    print("First appeared position is " + str(pos)) 

# 打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或读取和写入文件的模式（'r+'）。
# 如果省略了模式实参，Python将以默认的只读模式打开文件
file_name = "learningsource\pi-100digits.txt"
with open(file_name, 'w') as file_obj:
    # 将pi小数点后100位写入文件
    file_obj.write(pi_string[:102]) 

file_name = "learningsource\pi-500digits.txt"
with open(file_name, 'w') as file_obj:
    # 将pi小数点后500位写入文件，每行100位
    for i in range(0, 401, 100):
        if i == 0:
            file_obj.write(pi_string[i:i+102] + '\n') 
        else:
            file_obj.write(pi_string[i+2:i+102] + '\n') 

file_name = "learningsource\\add.txt"
with open(file_name, 'a') as file_obj:
    file_obj.write('这是新增的内容！\n') 
