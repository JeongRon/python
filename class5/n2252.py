'''
2252번 - 줄 세우기 / gold 3 / 위상 정렬
'''
from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


# 위상 정렬 알고리즘
def topology_sort():
    result = []
    que = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)
    while que:
        now = que.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                que.append(i)
    for i in result:
        print(i, end=' ')


topology_sort()
