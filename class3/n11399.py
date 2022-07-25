"""
11399 - ATM (silver 4)
"""
import sys

input = sys.stdin.readline

N = int(input())
wait_list = list(map(int, input().split()))
wait_list.sort()

wait = 0
result = 0
for i in range(N):
    wait += wait_list[i]
    result += wait
print(result)
