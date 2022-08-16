"""
1074 - Z (silver 1)
"""
import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())

num = 0

while n != 0:
    n -= 1

    # 1 사분면
    if a < 2**n and b < 2**n:
        num += (2**n) * (2**n) * 0
    # 2 사분면
    elif a < 2**n and b >= 2**n:
        num += (2**n) * (2**n) * 1
        b -= 2**n
    # 3 사분면
    elif a >= 2**n and b < 2**n:
        num += (2**n) * (2**n) * 2
        a -= 2**n
    # 4 사분면
    elif a >= 2**n and b >= 2**n:
        num += (2**n) * (2**n) * 3
        a -= 2**n
        b -= 2**n

print(num)
