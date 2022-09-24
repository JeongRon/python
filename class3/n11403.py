"""
11403 - 경로 찾기 (S1)

정점의 개수 : N
간선표시 - 행렬 : (i, j)
"""

# 1. 입력 코드
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
# 2. 값 구하기 / 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
# 3. 출력 코드
for i in range(N):
    for j in range(N):
        print(graph[i][j], end=" ")
    print()

# -------------------------------------------------------------
# 내가 푼 방식 / BFS (정답)
# from collections import deque


# def find_root(start, end):
#     que = deque(i for i in range(N) if graph[start][i] == 1)
#     visited = []
#     while que:
#         if end in que:
#             return 1
#         point = que.popleft()
#         visited.append(point)
#         for i in range(N):
#             if graph[point][i] == 1:
#                 if i not in visited:
#                     que.append(i)
#     return 0


# # 1. 입력 코드
# N = int(input())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input().split())))
# result = [[0 for _ in range(N)] for _ in range(N)]
# # 2. 값 구하기
# for i in range(N):
#     for j in range(N):
#         result[i][j] = find_root(i, j)
# # 3. 출력 코드
# for i in range(N):
#     for j in range(N):
#         print(result[i][j], end=" ")
#     print()
