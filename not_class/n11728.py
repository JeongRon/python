'''
11728번: 배열 합치기 / silver 5 / 정렬
'''
import sys

input = sys.stdin.readline

# 1. 입력 받기
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# 2. 두 배열 합친 후, 오름차순 정렬하기
arr_sum = a + b
arr_sum.sort()
# 3. 출력하기
for i in arr_sum:
    print(i, end=' ')
