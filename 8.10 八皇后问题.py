# 对于逐步得到结果的复杂递归算法，非常适合使用生成器来实现。
# 要在不使用生成器的情况下实现这些算法，通常必须通过额外的参数来传递部分结果，让递归调用能够接着往下计算
# 通过使用生成器，所有的递归调用都只需生成其负责部分的结果。可使用这种策略来遍历图结构和树结构
import random

# 检测冲突
def conflict(state, nextX):
    """state是状态元组，按顺序记录每个皇后的x坐标。"""
    # 计算y坐标，从0开始，因此等于已有皇后的个数
    nextY = len(state) 
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            # 如果位于同一列或水平距离等于垂直距离(位于一条对角线上)
            return True
    return False

def queens(num, state=()):
    '遍历所有可能的位置，并返回那些不会引发冲突的位置'
    # num为皇后总数，state是一个元组，表示已放好的皇后的位置
    if len(state) == num - 1:
        for pos in range(num):
            if not conflict(state, pos):
                yield (pos,)
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

# print(list(queens(4, (1, 3, 0))))
# print(list(queens(5)))

def line(pos, length):
    return '· ' * (pos) + '👑 ' + '· ' * (length - pos - 1)

def prettyprint(solution): 
    for pos in solution:
        print(line(pos, len(solution)))
 
#  打印随机一组结果
solution = random.choice(list(queens(8)))
prettyprint(solution)