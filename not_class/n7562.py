'''
7562 - 나이트의 이동 / silve 1 / BFS
'''
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs(l, now, res):
    board = [[INF for _ in range(l)] for _ in range(l)]
    que = deque()
    que.append((now[0], now[1], 0))
    while que:
        x, y, step = que.popleft()
        if x == res[0] and y == res[1]:
            break
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < l and 0 <= ny < l:
                if board[nx][ny] > step + 1:
                    que.append((nx, ny, step + 1))
                    board[nx][ny] = step + 1
    print(0 if board[x][y] == INF else board[x][y])


t = int(input())
for _ in range(t):
    l = int(input())
    now = list(map(int, input().split()))
    res = list(map(int, input().split()))
    bfs(l, now, res)
