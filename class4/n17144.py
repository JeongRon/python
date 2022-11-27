"""
17144 - 미세먼지 안녕! / gold 4 / 구현, 시뮬레이션
"""
import sys

input = sys.stdin.readline

r, c, t = map(int, input().split())

graph = []
machine_index = 0
for i in range(r):
    graph.append(list(map(int, input().split())))

for j in range(r):
    if graph[j][0] == -1:
        machine_index = j
        break

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs_dust():
    extra = [[0 for _ in range(c)] for _ in range(r)]
    extra[machine_index][0] = -1
    extra[machine_index + 1][0] = -1

    for x in range(r):
        for y in range(c):
            if graph[x][y] > 0:
                cnt = 0
                for index in range(4):
                    rx = x + dx[index]
                    ry = y + dy[index]
                    if 0 <= rx < r and 0 <= ry < c:
                        if extra[rx][ry] != -1:
                            cnt += 1
                            extra[rx][ry] = extra[rx][ry] + (graph[x][y] // 5)
                extra[x][y] = extra[x][y] + (graph[x][y] - (graph[x][y] // 5 * cnt))
    return extra


# 처음 공기청정기 작동
def machine_one():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    index = 0
    before = 0
    x, y = machine_index, 1
    while True:
        rx = x + dx[index]
        ry = y + dy[index]
        # 종료 조건
        if x == machine_index and y == 0:
            break
        if rx < 0 or rx >= r or ry < 0 or ry >= c:
            index += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = rx
        y = ry


# 두번째 공기청정기 작동
def machine_two():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    index = 0
    before = 0
    x, y = machine_index + 1, 1
    while True:
        rx = x + dx[index]
        ry = y + dy[index]
        if x == machine_index + 1 and y == 0:
            break
        if rx < 0 or rx >= r or ry < 0 or ry >= c:
            index += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = rx
        y = ry


while t:
    # 1. 미세먼지 확장
    graph = bfs_dust()
    # 2. 공기청정기 작동
    machine_one()
    machine_two()
    t -= 1

res = 0
for i in range(r):
    for value in graph[i]:
        if value > 0:
            res += value
print(res)
