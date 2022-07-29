"""
9375 - 패션왕 신해빈 (silver 3)
"""
import sys

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    fashion = {}
    cnt = 1

    for i in range(n):
        value, key = input().split()
        if key in fashion.keys():
            fashion[key] += 1
        else:
            fashion[key] = 1

    for value in fashion.values():
        cnt *= value + 1

    print(cnt - 1)
