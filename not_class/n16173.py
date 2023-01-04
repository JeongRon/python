'''
16173번 - 점프왕 쩰리 (Small) / silver 4 / BFS
'''
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = []
for _ in range(n):
    visited.append([False] * n)

dx = [1, 0]
dy = [0, 1]

def bfs(a, b, visited):
    que = deque()
    que.append((a, b))
    visited[a][b] = True
    while que:
        x, y= que.popleft()
        if arr[x][y] == -1:
            return 'HaruHaru'
        for i in range(2):
            nx = x + dx[i] * arr[x][y]
            ny = y + dy[i] * arr[x][y]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny] = True
    return 'Hing'

print(bfs(0, 0, visited))
