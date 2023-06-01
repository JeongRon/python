'''
15683번: 감시 / gold 4 / 백트래킹
'''
import sys

input = sys.stdin.readline


# cctv가 (x,y) 위치에서 inc 방향으로 볼 수 있는 위치들을 리턴하는 함수
def simulation_dir(x, y, graph, inc):
    dir = []
    tx, ty = x, y
    while 0 <= tx < N and 0 <= ty < M and graph[tx][ty] != 6:
        dir.append((tx, ty))
        tx += inc[0]
        ty += inc[1]
    return dir


# (x,y)위치 cctv가 감시 가능한 방향 정보 리턴하는 함수
def cctv_directions(x, y, cctv_num, graph):
    all_dir = []
    # 오, 왼, 위, 아래
    increase = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    if cctv_num == 1:
        for i in range(4):
            inc = increase[i]
            dir = simulation_dir(x, y, graph, inc)
            all_dir.append(dir)
    elif cctv_num == 2:
        idx = [(0, 1), (2, 3)]
        for i in range(2):
            inc = increase[idx[i][0]]
            dir = simulation_dir(x, y, graph, inc)
            inc = increase[idx[i][1]]
            dir += simulation_dir(x, y, graph, inc)
            all_dir.append(dir)
    elif cctv_num == 3:
        idx = [(0, 2), (1, 2), (0, 3), (1, 3)]
        for i in range(4):
            inc = increase[idx[i][0]]
            dir = simulation_dir(x, y, graph, inc)
            inc = increase[idx[i][1]]
            dir += simulation_dir(x, y, graph, inc)
            all_dir.append(dir)
    elif cctv_num == 4:
        idx = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        for i in range(4):
            inc = increase[idx[i][0]]
            dir = simulation_dir(x, y, graph, inc)
            inc = increase[idx[i][1]]
            dir += simulation_dir(x, y, graph, inc)
            inc = increase[idx[i][2]]
            dir += simulation_dir(x, y, graph, inc)
            all_dir.append(dir)
    elif cctv_num == 5:
        dir = []
        for i in range(4):
            inc = increase[i]
            dir += simulation_dir(x, y, graph, inc)
        all_dir.append(dir)
    return all_dir


# 모든 cctv에서 보이지 않는 spot 찾는 함수
def blind_spot(graph, cctv_lst):
    cctv_set = set()
    for cctv in cctv_lst:
        for x, y in cctv:
            cctv_set.add((x, y))
    blind_spot = N * M
    for x in range(N):
        for y in range(M):
            if (x, y) in cctv_set:
                blind_spot -= 1
            elif graph[x][y] == 6:
                blind_spot -= 1
    return blind_spot


# 백트래킹
def backtracking(x, y, graph):
    global res
    global cctv_lst
    if x == N - 1 and y == M:
        res.append(blind_spot(graph, cctv_lst))
        return
    if y == M:
        x += 1
        y = 0
    if 1 <= graph[x][y] <= 5:
        directions = cctv_directions(x, y, graph[x][y], graph)
        for dir in directions:
            cctv_lst.append(dir)
            backtracking(x, y + 1, graph)
            cctv_lst.pop()
    else:
        backtracking(x, y + 1, graph)


# 입력받기
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
# 백트래킹 통해서 결과값들 모두 구하기
res = []
cctv_lst = []
backtracking(0, 0, graph)
print(min(res))
