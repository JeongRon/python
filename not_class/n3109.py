'''
3109번: 빵집 / gold 2 / DFS, 그리디
'''
import sys

input = sys.stdin.readline

dx = [-1, 0, 1]


def solve(x, y):
    if y == C - 1:
        return True
    for i in range(3):
        nx = dx[i] + x
        if 0 <= nx < R and graph[nx][y + 1] == '.' and not visited[nx][y + 1]:
            visited[nx][y + 1] = True
            if solve(nx, y + 1):
                return True
    return False


R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(str, input().rstrip())))
visited = [[False for _ in range(C)] for _ in range(R)]

ans = 0
for i in range(R):
    if graph[i][0] == '.':
        if solve(i, 0):
            ans += 1
print(ans)
