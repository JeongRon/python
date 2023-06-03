'''
4991번: 로봇 청소기 / gold 1 / BFS, 백트래킹
'''
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 더러운 칸 접근 가능한지 확인
def bfs_check():
    visited = [[False for _ in range(w)] for _ in range(h)]
    que = deque()
    visited[rx][ry] = True
    que.append((rx, ry))
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != 'x' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny))
    # 더러운 칸 visited되어있는지 확인
    for (i, j) in dirty:
        if visited[i][j] == False:
            return False
    return True


# (x,y) -> (a,b) 까지 거리 구하는 함수
def move_distance(x, y, a, b):
    visited = [[False for _ in range(w)] for _ in range(h)]
    que = deque()
    visited[x][y] = True
    que.append((x, y, 0))
    while que:
        mx, my, dist = que.popleft()
        if mx == a and my == b:
            return dist
        for i in range(4):
            nx = dx[i] + mx
            ny = dy[i] + my
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] != 'x' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx, ny, dist + 1))


def backtracking(clean, all_move, i, visited):
    global min_res
    # 종료 조건
    if clean == len(dirty):
        if min_res > all_move:
            min_res = all_move
        return
    else:
        for j in range(len(dirty)):
            if all_move < min_res:
                # 방문하지 않은 칸만
                if visited[j] == False:
                    # 더러운 칸 좌표 (j)
                    visited[j] = True
                    if clean == 0:
                        backtracking(clean + 1, all_move + robot_dist[j], j,
                                     visited)
                    else:
                        backtracking(clean + 1, all_move + dirty_dist[i][j], j,
                                     visited)
                    visited[j] = False


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 그래프, 로봇 위치, 더러운 칸 정보
    rx, ry = -1, -1
    dirty = []
    graph = []
    for x in range(h):
        graph.append(list(map(str, input().rstrip())))
        for y in range(w):
            if graph[x][y] == 'o':
                rx, ry = x, y
            elif graph[x][y] == '*':
                dirty.append((x, y))
    # 더러운 칸 방문 가능한지 체크
    if bfs_check():
        # robot -> dirty 사이 거리 구하기
        robot_dist = [0 for _ in range(len(dirty))]
        for i in range(len(dirty)):
            a, b = dirty[i]
            robot_dist[i] = move_distance(rx, ry, a, b)
        # dirty -> dirty 사이 거리 구하기
        dirty_dist = [[0 for _ in range(len(dirty))]
                      for _ in range(len(dirty))]
        for i in range(len(dirty)):
            for j in range(len(dirty)):
                if i == j or dirty_dist[i][j] > 0:
                    continue
                p, q = dirty[i]
                a, b = dirty[j]
                dist = move_distance(p, q, a, b)
                dirty_dist[i][j] = dist
                dirty_dist[j][i] = dist
        min_res = int(1e9)
        dirty_visited = [False for _ in range(len(dirty))]
        backtracking(0, 0, 0, dirty_visited)
        print(min_res)
    else:
        print(-1)
