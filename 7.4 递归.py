import bisect

# 递归函数通常包含两部分：
#   基线条件（针对最小的问题）：满足这个条件时函数直接返回一个值
#   递归条件：包含一个或多个调用，这些调用旨在解决问题的一部分



# 阶乘
#   基线条件：1的阶乘为1
#   递归条件：对于大于1的数字n，其阶乘等于n-1的阶乘再乘以n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# 幂
#   基线条件：任何数字x的0次幂都是1
#   递归条件：n>0时，x的n次幂等于x的n-1次幂乘以x
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
    
print(power(2, 10))

# 二分查找
#   基线条件：如果上限和下限相同，说明他们都指向数字所在的位置，因此直接将数字返回
#   递归条件：找出区间的中间位置，再确定数字在左半部分还是右半部分，然后继续以此方式查找
def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1

    if lower == upper:
        assert number == sequence[lower]
        return lower
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [35, 64, 79, 21, 17, 37, 99, 78, 15, 8, 6, 44]
seq2 = [1, 2, 3, 3, 4, 5, 6, 7, 8]

print(search(sorted(seq), 35, 0, len(seq)-1))
print(search(sorted(seq), 21))

# 模块bisect提供了标准的二分查找实现
seq.sort()
print(seq)
print(bisect.bisect(seq, 21)) # 返回要插入元素在列表中的下标。假定列表是有序的。
print(bisect.bisect(seq2, 3))
print(bisect.bisect_left(seq2, 3))  # 默认将元素插到左边，所以返回的是插入到左边的下标
print(bisect.bisect_right(seq2, 3)) # 与 bisect_left 相反