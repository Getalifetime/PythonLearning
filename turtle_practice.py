from turtle import *

"""
# 绘制等边三角形
forward(100)
left(120)
forward(100)
left(120)
forward(100)"""

#绘制一个任意矩形
def draw_rectangle(a, b=''):
	'绘制一个长为a，宽为b的矩形，不指定b时则绘制边长为a的正方形'
	for side in range(1,5):
		if side % 2 == 0:
			if b == '':
				forward(a)
			else:
				penup()
				forward(b)
				pendown()
		else:
			forward(a)
		left(90)

draw_rectangle(200, 100)

right(180)
draw_rectangle(200)

left(180)
circle(100, 180)

exitonclick()

input("Press <Enter>")

"""
numbers = ['1', '2', '3', '4', '5', '6', '7']
numbers[0] = 11
print(numbers)

#练习
print('\n[Practice]:')
for val in range(1,21):
	print(val, end=" ")
	
num = [val for val in range(1,1000001)]
sum1 = sum(num)
print("\nsum(1,1000000) = ",sum1,", min = ",min(num), ", max = ",max(num))

odd = [val for val in range(1,20,2)]
print("odd =",odd)

#方法1
cube1 = []
for val in range(1,11):
	cube1.append(val**3)
print("cube1 =",cube1)

#方法2
cube2 = [val**3 for val in range(1,11)]
print("cube2 =",cube2)
"""