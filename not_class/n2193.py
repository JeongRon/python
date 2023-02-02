'''
2193번 - 이친수 / silver 3 / DP
'''
print(2**89)
n = int(input())
dp = [0 for _ in range(n + 1)]
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])
