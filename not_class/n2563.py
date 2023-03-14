'''
2563번: 색종이 / silver 5 / 구현
'''
import sys

input = sys.stdin.readline

# 1. n(색종이 수) 입력 / graph(도화지) 초기화
n = int(input())
graph = [[0 for _ in range(101)] for _ in range(101)]
# 2. col, row(색종이 좌표) 입력 / graph(도화지)에 색종이 붙이기(1로 변경)
for _ in range(n):
    col, row = map(int, input().split())
    row = 100 - row
    for i in range(row, row - 10, -1):
        for j in range(col, col + 10):
            graph[i][j] = 1
# 3. 결과값 도출
res = 0
for i in graph:
    res += sum(i)
print(res)
