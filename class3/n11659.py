"""
11659 - 구간 합 구하기 4 (silver 3)
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
prefix_sum = [0]

result = 0
for i in N_list:
    result += i
    prefix_sum.append(result)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
