'''
2110번: 공유기 설치 / gold 4 / 이분탐색
'''
import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

max_res = 0
start = 1
end = arr[-1] - arr[0]

while start <= end:
    mid = (start + end) // 2
    now = arr[0]
    count = 1
    for i in range(1, len(arr)):
        if arr[i] >= now + mid:
            count += 1
            now = arr[i]
    if count >= c:
        start = mid + 1
        max_res = mid
    else:
        end = mid - 1
print(max_res)
