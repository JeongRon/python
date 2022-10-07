"""
14500 - 테트로미노 (G4) 
"""
import sys

input = sys.stdin.readline

tetromino = 0


def one_line(x, y):
    global tetromino
    # 가로 일직선
    if col > y + 3:
        result = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x][y + 3]
        tetromino = max(tetromino, result)
    # 세로 일직선
    if row > x + 3:
        result = arr[x][y] + arr[x + 1][y] + arr[x + 2][y] + arr[x + 3][y]
        tetromino = max(tetromino, result)


def square(x, y):
    global tetromino
    # 정사각형
    if col > y + 1 and row > x + 1:
        result = arr[x][y] + arr[x + 1][y] + arr[x][y + 1] + arr[x + 1][y + 1]
        tetromino = max(tetromino, result)


def rectangle_col(x, y):
    global tetromino
    # 가로가 긴 직사각형
    if col > y + 2 and row > x + 1:
        # 1. 주황색 테트리스
        a = arr[x][y] + arr[x + 1][y] + arr[x][y + 1] + arr[x][y + 2]
        b = arr[x][y] + arr[x + 1][y] + arr[x + 1][y + 1] + arr[x + 1][y + 2]
        c = arr[x][y + 2] + arr[x + 1][y] + arr[x + 1][y + 1] + arr[x + 1][y + 2]
        d = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 2]
        # 2. 연두색 테트리스
        aa = arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y] + arr[x + 1][y + 1]
        bb = arr[x][y] + arr[x][y + 1] + arr[x + 1][y + 1] + arr[x + 1][y + 2]
        # 3. 분홍색 테트리스
        cc = arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 1]
        dd = arr[x][y + 1] + arr[x + 1][y] + arr[x + 1][y + 1] + arr[x + 1][y + 2]
        result = max(a, b, c, d, aa, bb, cc, dd)
        tetromino = max(tetromino, result)


def rectangle_row(x, y):
    global tetromino
    # 세로가 긴 직사각형
    if col > y + 1 and row > x + 2:
        # 1. 주황색 테트리스
        a = arr[x][y] + arr[x + 1][y] + arr[x + 2][y] + arr[x + 2][y + 1]
        b = arr[x][y] + arr[x][y + 1] + arr[x + 1][y + 1] + arr[x + 2][y + 1]
        c = arr[x][y] + arr[x][y + 1] + arr[x + 1][y] + arr[x + 2][y]
        d = arr[x][y + 1] + arr[x + 1][y + 1] + arr[x + 2][y] + arr[x + 2][y + 1]
        # 2. 연두색 테트리스
        aa = arr[x][y] + arr[x + 1][y] + arr[x + 1][y + 1] + arr[x + 2][y + 1]
        bb = arr[x][y + 1] + arr[x + 1][y + 1] + arr[x + 1][y] + arr[x + 2][y]
        # 3. 분홍색 테트리스
        cc = arr[x][y] + arr[x + 1][y] + arr[x + 2][y] + arr[x + 1][y + 1]
        dd = arr[x][y + 1] + arr[x + 1][y + 1] + arr[x + 1][y] + arr[x + 2][y + 1]
        result = max(a, b, c, d, aa, bb, cc, dd)
        tetromino = max(tetromino, result)


# 1. Input
row, col = map(int, input().split())
arr = []
for _ in range(row):
    arr.append(list(map(int, input().split())))
# 2. Search
for x in range(row):
    for y in range(col):
        one_line(x, y)
        square(x, y)
        rectangle_col(x, y)
        rectangle_row(x, y)

print(tetromino)
