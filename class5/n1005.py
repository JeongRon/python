'''
1005번 - ACM Craft / gold 3 / 위상정렬, DP
'''
import sys
from collections import deque

input = sys.stdin.readline


# 위상 정렬 알고리즘
def topology_sort():
    dp_cost = [0 for _ in range(n + 1)]
    que = deque()
    for index in range(1, n + 1):
        if in_degree[index] == 0:
            que.append(index)
            dp_cost[index] = build_cost[index]
    while que:
        now = que.popleft()
        if now == last_build:
            print(dp_cost[now])
            break

        for i in build_graph[now]:
            in_degree[i] -= 1
            if dp_cost[i] == 0:
                dp_cost[i] = dp_cost[now] + build_cost[i]
            else:
                if dp_cost[i] < dp_cost[now] + build_cost[i]:
                    dp_cost[i] = dp_cost[now] + build_cost[i]

            if in_degree[i] == 0:
                que.append(i)


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    build_cost = [0] + list(map(int, input().split()))
    build_graph = [[] for _ in range(n + 1)]
    in_degree = [0 for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        build_graph[a].append(b)
        in_degree[b] += 1
    last_build = int(input())
    topology_sort()
