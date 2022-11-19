'''
2206 - 벽 부수고 이동하기 / gold 3 / BFS
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

# 3차원 배열
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, z):
    que = deque()
    que.append((x, y, z))
    while que:
        a, b, c = que.popleft()
        # 종료조건
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        # 상하좌우
        for i in range(4):
            mx = dx[i] + a
            my = dy[i] + b
            if 0 <= mx < n and 0 <= my < m:
                if graph[mx][my] == 1 and c == 0:
                    visited[mx][my][1] = visited[a][b][0] + 1
                    que.append((mx, my, 1))
                elif graph[mx][my] == 0 and visited[mx][my][c] == 0:
                    visited[mx][my][c] = visited[a][b][c] + 1
                    que.append((mx, my, c))
    return -1


print(bfs(0, 0, 0))
