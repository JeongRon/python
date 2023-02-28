'''
2589번: 보물섬 / gold 5 / 브루트포스+BFS
'''
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 3. BFS / graph[x][y] 시작점에서 가장 먼 거리 구하기
def graph_bfs(short_path, x, y):
    max_dist = 0
    que = deque()
    que.append((x, y, 0))
    short_path[x][y] = 0
    while que:
        a, b, dist = que.popleft()
        if max_dist < dist:
            max_dist = dist
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] == 'L':
                    if short_path[nx][ny] == -1:
                        short_path[nx][ny] = dist + 1
                        que.append((nx, ny, dist + 1))
    return max_dist


# 1. 입력 받기 / r, c, graph
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

# 2. 브루트포스 / graph 의 모든 위치 확인하기
res = 0
for i in range(r):
    for j in range(c):
        short_path = [[-1 for _ in range(c)] for _ in range(r)]
        if graph[i][j] == 'L':
            max_dist = graph_bfs(short_path, i, j)
            if res < max_dist:
                res = max_dist
print(res)
