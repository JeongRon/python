"""
15652 - N과 M (4) / S(3)
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []


def dfs(start):
    if len(arr) == M:
        for value in arr:
            print(value, end=" ")
        print()
        return

    for num in range(start, N + 1):
        arr.append(num)
        dfs(num)
        arr.pop()


dfs(1)
