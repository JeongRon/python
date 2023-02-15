'''
7795번: 먹을 것인가 먹힐 것인가 / silver 3 / 이분탐색
'''
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    all_cnt = 0
    for i in range(len(a)):
        point = -1
        start = 0
        end = len(b) - 1
        while start <= end:
            mid = (start + end) // 2
            if b[mid] < a[i]:
                point = mid
                start = mid + 1
            else:
                end = mid - 1
        all_cnt += point + 1
    print(all_cnt)
