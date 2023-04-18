'''
1520번: 내리막 길 / gold 3 / DP, DFS
'''
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def dfs(x, y):
    # 목적지 도착시 -> 이동했던 칸들 1씩 더하기
    if x == n - 1 and y == m - 1:
        return 1
    # 아직 이동하지 않은 칸에 왔을 시, 상하좌우 탐색하기
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] < graph[x][y]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]


# 1. n, m, graph 입력 받기
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 2. dp 리스트 만들기
dp = [[-1 for _ in range(m)] for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# 3. DFS + DP 활용
print(dfs(0, 0))
