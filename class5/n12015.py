'''
12015번 - 가장 긴 증가하는 부분 수열 2 / gold 2 / bisect
'''
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
LIS = [arr[0]]

for num in arr:
    if LIS[-1] < num:
        LIS.append(num)
    else:
        LIS[bisect_left(LIS, num)] = num

print(len(LIS))
