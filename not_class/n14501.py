'''
14501번 - 퇴사 / silver 3 / DP
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n + 1)]
time = []
pay = []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)
# 마지막 인덱스 ~ 0 인덱스 까지
for i in range(n - 1, -1, -1):
    if i + time[i] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], pay[i] + dp[i + time[i]])
print(dp[0])
