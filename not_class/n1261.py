'''
1261번 - 알고스팟 / gold 4 / 다익스트라
'''
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
distance = [[INF for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
que = []
heapq.heappush(que, (0, 0, 0))
while que:
    step, x, y = heapq.heappop(que)
    if distance[x][y] > step:
        distance[x][y] = step
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    heapq.heappush(que, (step, nx, ny))
                elif graph[nx][ny] == 1:
                    heapq.heappush(que, (step + 1, nx, ny))

print(distance[n - 1][m - 1])
