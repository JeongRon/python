"""
15663 - N과 M (9) / S(2) / 백트래킹
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
input_list = list(map(int, input().split()))
input_list.sort()

visited = [False] * N
dfs_list = []


def dfs():
    if len(dfs_list) == M:
        for num in dfs_list:
            print(num, end=" ")
        print()
        return

    pre_num = 0
    for index in range(N):
        if not visited[index] and pre_num != input_list[index]:
            visited[index] = True
            dfs_list.append(input_list[index])
            pre_num = input_list[index]
            dfs()
            visited[index] = False
            dfs_list.pop()


dfs()
