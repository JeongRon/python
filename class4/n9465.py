"""
9465 - 스티커 / silver 1 / DP
"""
import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    # 1. Input
    n = int(input().rstrip())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split())))

    # 2. DP
    if n >= 2:
        dp[0][1] = dp[0][1] + dp[1][0]
        dp[1][1] = dp[1][1] + dp[0][0]
        for y in range(2, n):
            for x in range(2):
                dp[x][y] = dp[x][y] + max(dp[abs(x - 1)][y - 2], dp[abs(x - 1)][y - 1])
    # 3. Print
    print(max(dp[0][n - 1], dp[1][n - 1]))
