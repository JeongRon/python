'''
17404번 - RGB거리 2 / gold 4 / DP
'''
import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

min_value = INF
# 첫 인덱스에서 R,G,B 선택
for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = arr[0][i]
    # dp 알고리즘
    for j in range(1, n):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + arr[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + arr[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + arr[j][2]
    # 처음 선택한 i와 다른 인덱스 중 최소값 갱신
    for index in range(3):
        if index != i:
            min_value = min(min_value, dp[n - 1][index])

print(min_value)
