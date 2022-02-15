# 将以数字年月日的日期按格式打印
import encodings


months = [
    'jan',
    'feb',
    'mar',
    'apr',
    'may',
    'jun',
    'jul',
    'aug',
    'sep',
    'oct',
    'nov',
    'dec',
]

# 数字1-31对应的结尾
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
# 加号‘+’拼接序列，一般而言不能拼接不同类型的序列
# 将序列与数x相乘时，将重复这个序列x次来创建一个新序列
#print(endings)

while True:
    year = input('Year: ')
    if year.isdigit():
        break
    else:
        print("Please input a number!")

while True:
    month = input('Month(1-12): ')
    if month.isdigit():
        month_num = int(month)
        if(month_num > 0 and month_num <= 12):
            break
    else:
        print("Please input a number(1-12)!")

while True:
    day = input('Day(1-31): ')
    if day.isdigit():
        day_num = int(day)
        if(day_num > 0 and day_num <= 31):
            break
    else:
        print("Please input a number(1-31)!")

month_name = months[month_num-1]
ordinal = day + endings[day_num-1]

print(month_name.title() + ' ' + ordinal + ', ' + year)