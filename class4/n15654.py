"""
15654 - N과 M (5) / S(3)
"""

import sys

input = sys.stdin.readline

# 1. Input
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()

dfs_list = []

# 2. Dfs Function
def dfs():
    if len(dfs_list) == M:
        for num in dfs_list:
            print(num, end=" ")
        print()
        return

    for index in range(N):
        if input_list[index] not in dfs_list:
            dfs_list.append(input_list[index])
            dfs()
            dfs_list.pop()


dfs()
