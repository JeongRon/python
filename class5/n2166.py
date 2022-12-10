"""
2166번 - 다각형의 면적 / gold 5 / abs, round
"""
import sys

input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.append(arr[0])

res = 0
for i in range(n):
    res += (arr[i][0] * arr[i + 1][1]) - (arr[i][1] * arr[i + 1][0])

res = round(res / 2, 1)

print(abs(res))
