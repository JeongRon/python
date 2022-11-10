"""
17070 - 파이프 옮기기 1 / gold 5 / DFS
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

count = 0

# 현재 방향 (1:row, 2:dia, 3:col) / 좌표 x, y
def dfs(direction, x, y):
    global count
    # count (last index)
    if x == n - 1 and y == n - 1:
        count += 1
    else:
        # row
        if direction == 1:
            # row
            if y + 1 < n and arr[x][y + 1] == 0:
                dfs(1, x, y + 1)
            # dia
            if (
                x + 1 < n
                and y + 1 < n
                and arr[x][y + 1] == 0
                and arr[x + 1][y] == 0
                and arr[x + 1][y + 1] == 0
            ):
                dfs(2, x + 1, y + 1)
        # dia
        elif direction == 2:
            # row
            if y + 1 < n and arr[x][y + 1] == 0:
                dfs(1, x, y + 1)
            # dia
            if (
                x + 1 < n
                and y + 1 < n
                and arr[x][y + 1] == 0
                and arr[x + 1][y] == 0
                and arr[x + 1][y + 1] == 0
            ):
                dfs(2, x + 1, y + 1)
            # col
            if x + 1 < n and arr[x + 1][y] == 0:
                dfs(3, x + 1, y)
        # col
        elif direction == 3:
            # dia
            if (
                x + 1 < n
                and y + 1 < n
                and arr[x][y + 1] == 0
                and arr[x + 1][y] == 0
                and arr[x + 1][y + 1] == 0
            ):
                dfs(2, x + 1, y + 1)
            # col
            if x + 1 < n and arr[x + 1][y] == 0:
                dfs(3, x + 1, y)


dfs(1, 0, 1)
print(count)
