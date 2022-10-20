"""
12865 - 평범한 배낭 / gold 5 / DP(Knapsack)
"""
import sys

input = sys.stdin.readline

# 1. Input
n, k = map(int, input().split())
stuff = [[0, 0]]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for _ in range(n):
    stuff.append(list(map(int, input().split())))

# 2. DP(Knapsack)
for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

# 3. Print
print(dp[n][k])
