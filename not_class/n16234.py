'''
16234번: 인구 이동 / gold 5 / 구현, 시뮬레이션
'''
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                if L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                    graph_info.append([nx, ny])
                    graph_num.append(graph[nx][ny])
                    dfs(nx, ny)


# 입력받기
N, L, R = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 시뮬레이션
turn = 0
while True:
    change_graph = False
    visited = [[False for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                # 현재 국가 graph[x][y] 와 국경개방 하는 나라 찾기
                graph_info = [[x, y]]
                graph_num = [graph[x][y]]
                # dfs로 국경개방 나라 정보 담기
                dfs(x, y)
                if len(graph_num) >= 2:
                    change_graph = True
                div_num = sum(graph_num) // len(graph_num)
                for p, q in graph_info:
                    graph[p][q] = div_num
    if not change_graph:
        break
    else:
        turn += 1
print(turn)
