"""
11726 - 2×n 타일링 (silver 3)
"""
import sys

input = sys.stdin.readline

dp = [0, 1, 2]
n = int(input().rstrip())
for i in range(3, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[n] % 10007)