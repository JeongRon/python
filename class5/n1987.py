"""
1987번 - 알파벳 / gold 4 / DFS
"""
import sys

input = sys.stdin.readline

row, col = map(int, input().split())
graph = []
for _ in range(row):
    graph.append(list(input().rstrip()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

res = 0
visited = set(graph[0][0])


def dfs(x, y):
    global res
    if res < len(visited):
        res = len(visited)
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < row and 0 <= ny < col:
            if graph[nx][ny] not in visited:
                visited.add(graph[nx][ny])
                dfs(nx, ny)
                visited.remove(graph[nx][ny])


dfs(0, 0)

print(res)
