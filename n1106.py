'''
1106번 - 호텔 / gold 5 / DP-배낭
'''
import sys

INF = int(1e9)
input = sys.stdin.readline

# 1. 입력 및 리스트 만들기
all_customer, all_city = map(int, input().split())

info = [(0, 0)]
for _ in range(all_city):
    cost, customer = map(int, input().split())
    info.append((cost, customer))

dp = [[INF for _ in range(all_customer + 1)] for _ in range(all_city + 1)]

# 2. DP-배낭 알고리즘
for i in range(1, all_city + 1):
    city_cost, city_customer = info[i]
    mul = 1
    for j in range(1, all_customer + 1):
        if j < city_customer:
            dp[i][j] = min(dp[i - 1][j], city_cost)
        else:
            dp[i][j] = min(dp[i - 1][j], city_cost * mul,
                           dp[i][j - city_customer] + dp[i][city_customer])
            if j % city_customer == 0:
                mul += 1

print(dp[-1][-1])
