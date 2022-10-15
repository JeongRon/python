"""
11053 - 가장 긴 증가하는 부분 수열 / S(2) / DP
"""
import sys

input = sys.stdin.readline

N = int(input().rstrip())
input_list = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if input_list[i] > input_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

"""
<<입력>>
6
10 20 10 30 20 50
<<DP>>
[1, 2, 1, 3, 2, 4]

인덱스(i) 기준으로 / 전 인덱스의(j) 값이랑 비교
"""
