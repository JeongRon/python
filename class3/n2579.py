"""
2579 - 계단 오르기 (silver 3)
"""
import sys

input = sys.stdin.readline

stairs = [0] * 301
dp = [0] * 301
n = int(input().rstrip())

for i in range(1, n + 1):
    stairs[i] = int(input().rstrip())

dp[1] = stairs[1]
dp[2] = stairs[2] + stairs[1]
dp[3] = max(stairs[3] + stairs[2], stairs[3] + stairs[1])
for j in range(4, n + 1):
    dp[j] = max(stairs[j] + stairs[j - 1] + dp[j - 3], stairs[j] + dp[j - 2])

print(dp[n])
