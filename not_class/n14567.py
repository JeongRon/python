'''
14567번 - 선수과목 (Prerequisite) / gold 5 / 위상정렬
'''
import sys
from collections import deque

input = sys.stdin.readline


def topology_sort():
    sort_result = [0 for _ in range(n + 1)]
    que = deque()
    for sub_num in range(1, n + 1):
        if in_degree[sub_num] == 0:
            que.append((sub_num, 1))
            sort_result[sub_num] = 1
    while que:
        subject, sort_num = que.popleft()
        for next_subject in graph[subject]:
            in_degree[next_subject] -= 1
            if in_degree[next_subject] == 0:
                que.append((next_subject, sort_num + 1))
                sort_result[next_subject] = sort_num + 1
    for index in range(1, n + 1):
        print(sort_result[index], end=' ')


n, m = map(int, input().split())
in_degree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

topology_sort()
