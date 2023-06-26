'''
17136번: 색종이 붙이기 / gold 2 / 백트래킹
'''
import sys

input = sys.stdin.readline

# 그래프 입력
graph = []
for _ in range(10):
    graph.append(list(map(int, input().split())))
remain = [0, 5, 5, 5, 5, 5]
result = 26


def check_cover(x, y, k):
    rx, ry = x + k, y + k
    if rx > 10 or ry > 10:
        return False
    for nx in range(x, rx):
        for ny in range(y, ry):
            if graph[nx][ny] != 1:
                return False
    return True


def change_graph(x, y, k, num):
    for i in range(x, x + k):
        for j in range(y, y + k):
            graph[i][j] = num


def backtracking(x, y, cnt):
    global result
    if x == 10:
        result = min(result, cnt)
        return
    if y == 10:
        backtracking(x + 1, 0, cnt)
        return
    if graph[x][y] == 1:
        for k in range(1, 6):
            if remain[k] == 0:
                continue
            if check_cover(x, y, k) == True:
                remain[k] -= 1
                change_graph(x, y, k, 0)
                backtracking(x, y + 1, cnt + 1)
                remain[k] += 1
                change_graph(x, y, k, 1)
    else:
        backtracking(x, y + 1, cnt)


backtracking(0, 0, 0)
if result == 26:
    print(-1)
else:
    print(result)
