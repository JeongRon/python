"""
15666 - N과 M (9) / S(2) / 백트래킹
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
temp = set(map(int, input().split()))
input_list = sorted(list(temp))
dfs_list = []


def dfs(start):
    if len(dfs_list) == M:
        for num in dfs_list:
            print(num, end=" ")
        print()
        return

    for index in range(start, len(input_list)):
        dfs_list.append(input_list[index])
        dfs(index)
        dfs_list.pop()


dfs(0)
