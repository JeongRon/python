'''
2210번 - 숫자판 점프 / silver 2 / DFS
'''
import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, stack):
    stack += str(arr[x][y])
    if len(stack) == 6:
        case.add(int(stack))
    else:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 5 and 0 <= ny < 5:
                dfs(nx, ny, stack)


arr = []
for _ in range(5):
    arr.append(list(map(int, input().split())))
case = set()

for i in range(5):
    for j in range(5):
        stack = ''
        dfs(i, j, stack)

print(len(case))
