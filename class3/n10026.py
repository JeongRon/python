"""
10026 - 적록색약 (G5)
"""
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y):
    visited[x][y] = 1
    color = painting[x][y]
    for i in range(4):
        move_x = x + dx[i]
        move_y = y + dy[i]
        if 0 <= move_x < N and 0 <= move_y < N:
            if visited[move_x][move_y] == 0 and painting[move_x][move_y] == color:
                dfs(move_x, move_y)


# 1. Input
painting = []
N = int(input().rstrip())
for _ in range(N):
    painting.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(N)] for _ in range(N)]
cnt = [0, 0]

# 2. First - DFS
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt[0] += 1

# 3. change painting value : R-value -> G-value
for i in range(N):
    for j in range(N):
        if painting[i][j] == "R":
            painting[i][j] = "G"

# 3. initialization visited list
visited = [[0 for _ in range(N)] for _ in range(N)]

# 4. Second - DFS
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            cnt[1] += 1
# 5. print : cnt value
print(cnt[0], cnt[1])
