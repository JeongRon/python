"""
10826 - 피보나치 수 4 / silver 5 / dp
"""

n = int(input())

dp = [0, 1]

for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[n])
