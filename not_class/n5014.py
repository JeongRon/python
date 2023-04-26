'''
5014번: 스타트링크 / silver 1 / BFS
'''
from collections import deque

# 입력받기
max_floor, start, end, up, down = map(int, input().split())
# que, visited 리스트 선언 및 초기화
que = deque()
visited = list(0 for _ in range(max_floor + 1))
que.append((start))
visited[start] = 1
# BFS 알고리즘
while que:
    now_floor = que.popleft()
    if now_floor == end:
        print(visited[end] - 1)
        exit()
    for next_floor in (now_floor + up, now_floor - down):
        if 0 < next_floor <= max_floor and visited[next_floor] == 0:
            visited[next_floor] = visited[now_floor] + 1
            que.append(next_floor)
if visited[end] == 0:
    print('use the stairs')
