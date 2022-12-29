"""
2473번 - 세 용액 / gold 3 / 투 포인터
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

min_value = sys.maxsize
zero_flag = False

for fix_index in range(n - 2):
    if zero_flag:
        break
    start = fix_index + 1
    end = n - 1

    while start < end:
        tmp_value = arr[start] + arr[end] + arr[fix_index]
        tmp_abs = abs(arr[start] + arr[end] + arr[fix_index])

        if tmp_abs < min_value:
            min_value = tmp_abs
            min_fix = arr[fix_index]
            min_start = arr[start]
            min_end = arr[end]

        if tmp_value > 0:
            end -= 1
        elif tmp_value < 0:
            start += 1
        else:
            zero_flag = True
            break

print(min_fix, min_start, min_end)
