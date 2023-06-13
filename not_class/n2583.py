'''
2583번: 영역 구하기 / silver 1 / DFS
'''
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)


# x,y ~ a,b 꼭짓점 직사각형 graph에 넣는 함수
def put_square(y, x, b, a):
    for i in range(x, a):
        for j in range(y, b):
            graph[i][j] = 2


# graph에 연속된 빈 공간 찾고 넓이 리턴하는 함수
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global cnt
    graph[x][y] = 3
    cnt += 1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                dfs(nx, ny)


# 입력받기
N, M, K = map(int, input().split())
square = []
for _ in range(K):
    square.append(list(map(int, input().split())))
# N*M 그래프 만들기
graph = [[0 for _ in range(M)] for _ in range(N)]
# 그래프에 K 영역 대입하기
for i in range(K):
    x, y, a, b = square[i]
    put_square(x, y, a, b)
# 빈 공간 체크
empty_space = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            cnt = 0
            dfs(i, j)
            empty_space.append(cnt)
# 출력하기
empty_space.sort()
print(len(empty_space))
for v in empty_space:
    print(v, end=' ')
