'''
2239번 - 스도쿠 / gold 4 / 백트래킹, DFS
'''
import sys

input = sys.stdin.readline

arr = []
zero_index = []
for i in range(9):
    arr.append(list(map(int, input().rstrip())))
    for j in range(9):
        if arr[i][j] == 0:
            zero_index.append((i, j))
zero_cnt = len(zero_index)


def input_num(x, y, num):
    for i in range(9):
        if arr[x][i] == num:
            return False
    for j in range(9):
        if arr[j][y] == num:
            return False
    n = (x // 3) * 3
    m = (y // 3) * 3
    for a in range(3):
        for b in range(3):
            if arr[n + a][m + b] == num:
                return False
    return True


def backtracking(idx):
    if idx == zero_cnt:
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end='')
            print()
        exit()

    x, y = zero_index[idx]
    for num in range(1, 10):
        if input_num(x, y, num):
            arr[x][y] = num
            backtracking(idx + 1)
            arr[x][y] = 0


backtracking(0)
