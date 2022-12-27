'''
10942 - 팰린드롬? / gold 4 / DP
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

dp = [[0 for _ in range(n)] for _ in range(n)]

# 길이가 1인 경우
for i in range(n):
    dp[i][i] = 1
# 길이가 2인 경우
for i in range(n - 1):
    if arr[i] == arr[i + 1]:
        dp[i][i + 1] = 1
# 길이가 3이상인 경우
for i in range(2, n):
    for j in range(n - i):
        if arr[j] == arr[i + j] and dp[j + 1][i + j - 1] == 1:
            dp[j][i + j] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
