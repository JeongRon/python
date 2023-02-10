'''
10211번 : Maximum Subarray / silver 4 / 누적합
'''
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # 누적합 구하기
    pre_sum = [0 for _ in range(n)]
    pre_sum[0] = arr[0]
    for i in range(1, n):
        pre_sum[i] = pre_sum[i - 1] + arr[i]
    # 누적합 활용 최대 부분배열 도출
    max_res = arr[0]
    for x in range(n):
        for y in range(x, n):
            if x == 0:
                res = pre_sum[y]
            else:
                res = pre_sum[y] - pre_sum[x - 1]
            if max_res < res:
                max_res = res
    print(max_res)
