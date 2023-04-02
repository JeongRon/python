'''
2740번: 행렬 곱셈 / silver 5 / 구현
'''
import sys

input = sys.stdin.readline

# 1. a, b 리스트 입력 받기
a = []
n, m = map(int, input().split())
for _ in range(n):
    a.append(list(map(int, input().split())))
b = []
m, k = map(int, input().split())
for _ in range(m):
    b.append(list(map(int, input().split())))
# 2. c 리스트 만들기 (a*b=c)
c = [[0 for _ in range(k)] for _ in range(n)]
for x in range(n):
    for y in range(k):
        tmp = 0
        for z in range(m):
            tmp += a[x][z] * b[z][y]
        c[x][y] = tmp
        print(c[x][y], end=' ')
    print()
