"""
1567 - N과 M (8) / S(3)
"""
import sys

input = sys.stdin.readline

# 1. Input
N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()
dfs_list = []

# 2. dfs function
def dfs(start):
    if len(dfs_list) == M:
        for num in dfs_list:
            print(num, end=" ")
        print()
        return

    for index in range(start, N):
        dfs_list.append(input_list[index])
        dfs(index)
        dfs_list.pop()


dfs(0)
