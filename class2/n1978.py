"""
1978 - 소수 찾기 (silver 5)
"""
import sys

N = int(sys.stdin.readline())
num_index = list(map(int, sys.stdin.readline().split()))

count = 0
for num in num_index:
    i = 1
    while i < num:
        i += 1
        if num == 2:
            count += 1
            break
        if i == num:
            count += 1
        if num % i == 0:
            break
print(count)
