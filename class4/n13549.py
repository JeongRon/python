"""
13549 - 숨바꼭질 3 / gold 5 / BFS
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001

que = deque()
que.append(n)
visited = [-1] * MAX
visited[n] = 0

while que:
    point = que.popleft()
    # 종료 조건
    if point == k:
        print(visited[point])
        break
    if 0 < point * 2 < MAX and visited[point * 2] == -1:
        visited[point * 2] = visited[point]
        que.appendleft(point * 2)
    if 0 <= point - 1 < MAX and visited[point - 1] == -1:
        visited[point - 1] = visited[point] + 1
        que.append(point - 1)
    if 0 <= point + 1 < MAX and visited[point + 1] == -1:
        visited[point + 1] = visited[point] + 1
        que.append(point + 1)
