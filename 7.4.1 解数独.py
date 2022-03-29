# sudoku = [
#     [0, 3, 1, 0, 0, 0, 4, 0, 0],
# 	[0, 4, 0, 0, 0, 0, 0, 5, 2],
# 	[0, 0, 0, 5, 0, 0, 0, 0, 0],
# 	[0, 0, 6, 1, 0, 0, 2, 0, 0],
# 	[0, 1, 0, 3, 0, 6, 0, 0, 0],
# 	[7, 0, 0, 2, 0, 0, 0, 9, 1],
# 	[9, 0, 0, 0, 0, 0, 0, 7, 0],
# 	[0, 0, 0, 0, 6, 0, 0, 0, 0],
# 	[0, 0, 0, 9, 0, 8, 0, 0, 5]
# ]

sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0]
]



# 检测是否有效
def isValid(su, row, column, num):

    # 判断所在行是否有重复的数字
    if num in su[row]:
        return False

    for i in range(9):
        # 判断所在列是否有重复的数字
        if su[i][column] == num:
            return False

	    # 判断所在的3x3方格是否有重复的数字
        if su[3 * (row // 3) + i // 3][3 * (column // 3) + i % 3] == num:
            return False
            
    return True

sum = 0

def solve_sudoku(su):	
    global sum

    for i in range(9):
        for j in range(9):
            if (su[i][j] == 0):
                for num in range(1, 10):
                    if isValid(su, i, j, num):
                        su[i][j] = num
                        sum += 1
                        if solve_sudoku(su):
                            return True
                        su[i][j] = 0
                return False
    print("\n共计尝试" + str(sum) + "次")
    return True

def print_sudoku(su):
    for row in range(9):
        print(su[row])
    # print('\n')

if __name__ == '__main__':
    print_sudoku(sudoku)
    solve_sudoku(sudoku)
    print_sudoku(sudoku)