'''
2580번: 스도쿠 / gold 4 / 백트래킹
'''
import sys

input = sys.stdin.readline


def check_col(x, v):
    for col in range(9):
        if graph[x][col] == v:
            return False
    return True


def check_row(y, v):
    for row in range(9):
        if graph[row][y] == v:
            return False
    return True


def check_square(x, y, v):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            if graph[i][j] == v:
                return False
    return True


def dfs(depth):
    # 3-1. 종료 조건 만족 시, 출력
    if depth == len(empty):
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end=' ')
            print()
        exit(0)
    # 3-2. 백트래킹 / empty 리스트에서 depth 번째 인덱스 좌표 불러오기 -> 1~9 숫자 넣기
    for v in range(1, 10):
        x, y = empty[depth]
        if check_col(x, v) and check_row(y, v) and check_square(x, y, v):
            graph[x][y] = v
            dfs(depth + 1)
            graph[x][y] = 0


# 1. 입력 받기 / graph
graph = []
for _ in range(9):
    graph.append(list(map(int, input().split())))
# 2. 빈칸(0) 좌표 empty 리스트에 넣기
empty = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            empty.append((i, j))
# 3. dfs 깊이 우선 탐색 실행
dfs(0)
