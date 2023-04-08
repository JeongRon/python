'''
13460번: 구슬 탈출 2 / gold 1 / BFS, 시뮬레이션
'''
import sys
from collections import deque

input = sys.stdin.readline
# 1. n, m, graph 입력 받기 + red, blue 위치 저장 하기
n, m = map(int, input().split())
graph = []
red = [0, 0]
blue = [0, 0]
for i in range(n):
    graph.append(list(input().rstrip()))
    for j in range(m):
        # 위치 저장 후, '.'으로 표시
        if graph[i][j] == 'R':
            red[0], red[1] = i, j
            graph[i][j] = '.'
        # 위치 저장 후, '.'으로 표시
        elif graph[i][j] == 'B':
            blue[0], blue[1] = i, j
            graph[i][j] = '.'

# 2. BFS 알고리즘
location = deque()
# location / 빨강_파랑 위치, 움직인 횟수 넣기
location.append((red[0], red[1], blue[0], blue[1], 0))
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 4가지 방향에 대해서 움직이고, append / (구멍 들어가면 append X)
while location:
    # (좌표)와 (움직인 횟수) 받기
    rx, ry, bx, by, move = location.popleft()
    # 움직인 횟수가 10번이라면 종료
    if move == 10:
        print(-1)    
        exit()
    # 상하좌우 하나씩 쭉 움직이기
    for i in range(4):
        red_goal = False
        blue_goal = False
        red_cnt = 0
        blue_cnt = 0
        nrx, nry = rx, ry
        nbx, nby = bx, by
        # 빨간 구슬 'O','#' 만나기 전까지 쭉 밀기
        while graph[nrx + dx[i]][nry + dy[i]] == '.':
            nrx += dx[i]
            nry += dy[i]
            red_cnt += 1
        # 파란 구슬 'O','#' 만나기 전까지 쭉 밀기
        while graph[nbx + dx[i]][nby + dy[i]] == '.':
            nbx += dx[i]
            nby += dy[i]
            blue_cnt += 1
        # 'O' 만났을 시 처리
        if graph[nrx + dx[i]][nry + dy[i]] == 'O':
            red_goal = True
        if graph[nbx + dx[i]][nby + dy[i]] == 'O':
            blue_goal = True
        # 빨간 구슬만 들어가면 바로 종료하기
        if red_goal == True and blue_goal == False:
            print(move + 1)
            exit()
        # 파란구슬이 들어가면 실패처리
        if blue_goal == True:
            continue
        # 방향 쭉 이동했는데, 좌표가 같을시 처리
        if nrx == nbx and nry == nby:
            if red_cnt > blue_cnt:
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]
        # 빨,파 구슬이 구멍에 안들어 왔을 경우 / 움직인 좌표 append
        location.append((nrx, nry, nbx, nby, move + 1))
