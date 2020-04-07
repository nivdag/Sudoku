import numpy as np

grid = [
    [4, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 9, 8],
    [3, 0, 0, 0, 8, 2, 4, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 8, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 6, 7, 0],
    [0, 5, 0, 0, 0, 9, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 9, 0, 7],
    [6, 4, 0, 3, 0, 0, 0, 0, 0],
]


def is_possible(row, column, number):
    global grid
    for i in range(0, 9):
        if grid[row][i] == number:
            return False
    for i in range(0, 9):
        if grid[i][column] == number:
            return False
    y = (row // 3) * 3
    x = (column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y + i][x + j] == number:
                return False
    return True


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if is_possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.array(grid))
    input("more solutions")


solve()
