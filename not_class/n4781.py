'''
4781번 - 사탕 가게 / gold 4 / DP-배낭
'''
import sys

input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n = int(n)
    if n == 0 and m == 0.00:
        break
    m = int(m * 100)

    info = [(0, 0)]
    dp = [0] * 10001

    for _ in range(n):
        c, p = map(float, input().split())
        info.append((int(c), int(p * 100 + 0.5)))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cal, price = info[j]
            if i < price:
                continue
            dp[i] = max(dp[i], cal + dp[i - price])

    print(dp[m])
