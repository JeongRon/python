"""
11725 - 트리의 부모 찾기 / Silver 2 / BFS
"""
import sys
from collections import deque

input = sys.stdin.readline

# 1. tree 딕셔너리에 연결된 노드 정보 담기
tree = dict()
N = int(input().rstrip())
for _ in range(N - 1):
    x, y = map(int, input().split())
    if x in tree:
        tree[x].append(y)
    else:
        tree[x] = [y]
    if y in tree:
        tree[y].append(x)
    else:
        tree[y] = [x]

# 2. bfs / queue 활용
# parent_node : 인덱스는 노드, 값은 부모 노드
# ex) parent_node[2] = 4 이면, 2번 노드의 부모 노드는 4이다. 라는 뜻
# visited : 각 인덱스 노드들이 방문된 녀석들인지
# que : bfs 형식으로 노드들을 append,popleft
parent_node = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
que = deque()
que.append(1)
while que:
    v = que.popleft()
    visited[v] = True
    for value in tree[v]:
        if not visited[value]:
            parent_node[value] = v
            que.append(value)

# 3. print
for i in range(2, N + 1):
    print(parent_node[i])
