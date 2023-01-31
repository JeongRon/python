'''
1026 - 보물 / silver 4 / 정렬, 그리디
'''
import sys

input = sys.stdin.readline

# 1. 입력 받기
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 2. a 리스트는 오름차순, b 리스트는 내림차순
a.sort()
b.sort(reverse=True)
# 3. 계산
res = 0
for i in range(n):
    res += a[i] * b[i]
print(res)
