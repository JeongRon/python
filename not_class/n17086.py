'''
17086번: 아기 상어 / silver 2 / BFS
'''
import sys
from collections import deque

input = sys.stdin.readline

# 1. n, m, graph 입력 받기 / 상어 위치 find 리스트에 담기
n, m = map(int, input().split())
find = deque()
graph = []
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(m):
        if graph[x][y] == 1:
            find.append((x, y))

# 2. graph 색칠하기 (BFS)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
while find:
    x, y = find.popleft()
    now_value = graph[x][y]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                graph[nx][ny] = now_value + 1
                find.append((nx, ny))
# 3. graph 에서 가장 큰 숫자 찾고, -1 해서 출력하기
max_res = 0
for lst in graph:
    if max_res < max(lst):
        max_res = max(lst)
print(max_res - 1)
