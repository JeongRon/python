'''
2294번: 동전 2 / gold 5 / DP
'''
INF = int(1e9)

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [INF for _ in range(k + 1)]
dp[0] = 0
for c in coin:
    for i in range(1, k + 1):
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
