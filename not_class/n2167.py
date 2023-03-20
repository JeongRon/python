'''
2167번: 2차원 배열의 합 / silver 5 / 구현
'''
import sys

input = sys.stdin.readline
# 1. 입력 받기 n, m, graph
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 2. k번 반복 / (i,j)~(x,y) 사이의 있는 좌표들 모두 더하기
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    i, j, x, y = i - 1, j - 1, x - 1, y - 1
    res = 0
    for row in range(i, x + 1):
        for col in range(j, y + 1):
            res += graph[row][col]
    print(res)
