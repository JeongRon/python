'''
2467번 - 용액 / gold 5 / 투 포인터
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

min_sum = sys.maxsize
start = 0
end = n - 1
while start < end:
    tmp_sum = arr[start] + arr[end]

    if abs(tmp_sum) < min_sum:
        min_sum = abs(tmp_sum)
        min_start = arr[start]
        min_end = arr[end]

    if tmp_sum > 0:
        end -= 1
    elif tmp_sum < 0:
        start += 1
    else:
        break

print(min_start, min_end)
