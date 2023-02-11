'''
10825번: 국영수 / silver 4 / 정렬
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))
arr.sort(key=lambda x: str(x[0]))
arr.sort(key=lambda x: int(x[3]), reverse=True)
arr.sort(key=lambda x: int(x[2]))
arr.sort(key=lambda x: int(x[1]), reverse=True)

for i in arr:
    print(i[0])
