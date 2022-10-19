"""
11660 - 구간 합 구하기 5 / silver 1 / DP
"""
import sys

input = sys.stdin.readline


# 1. Input
n, m = map(int, input().split())

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 2. DP / 구간 합
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j]) + arr[i][j]

# 3. 출력
for _ in range(m):
    x, y, p, q = map(int, input().split())
    print(dp[p][q] - (dp[x - 1][q] + dp[p][y - 1] - dp[x - 1][y - 1]))
