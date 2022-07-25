"""
11047 - 동전 0 (silver 4)
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coin_list = []
result = 0
for i in range(N):
    coin_list.append(int(input()))

for i in reversed(coin_list):
    result += K // i
    K = K % i

print(result)
