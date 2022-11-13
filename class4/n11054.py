"""
11054 - 가장 긴 바이토닉 부분 수열 / gold 4 / DP
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

up_dp = [1] * n
down_dp = [1] * n

# up_dp : 오름차순 가장 긴 수열 값들 저장
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            up_dp[i] = max(up_dp[i], up_dp[j] + 1)

# down_dp : 내림차순 가장 긴 수열 값들 저장
for i in range(-2, -n - 1, -1):
    for j in range(-1, i, -1):
        if arr[i] > arr[j]:
            down_dp[i] = max(down_dp[i], down_dp[j] + 1)

# result_dp : 오름차순 + 내림차순 가장 긴 수열 값 저장
result_dp = [0] * n
for i in range(n):
    result_dp[i] = up_dp[i] + down_dp[i] - 1

print(max(result_dp))
