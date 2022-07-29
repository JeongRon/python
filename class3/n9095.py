"""
9095 - 1, 2, 3 더하기 (silver 3)
"""
import sys

input = sys.stdin.readline

COUNT = 0


def dfs(N):
    global COUNT
    for i in range(1, 4):
        if N > i:
            dfs(N - i)
        elif N == i:
            COUNT += 1


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    dfs(N)
    print(COUNT)
    COUNT = 0
