'''
2293번: 동전 1 / gold 5 / DP
'''
import sys

input = sys.stdin.readline

# n, k, coin_list 입력받기
n, k = map(int, input().split())
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))
# DP 리스트 초기화
dp = [0 for _ in range(k + 1)]
dp[0] = 1
# DP 리스트 갱신하기
for coin in coin_list:
    for value in range(coin, k + 1):
        if value - coin >= 0:
            dp[value] += dp[value - coin]
# 출력하기
print(dp[k])
