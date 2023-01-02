'''
2143번 - 두 배열의 합 / gold 3 / dict 활용
'''
import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
n = int(input())
a_arr = list(map(int, input().split()))
m = int(input())
b_arr = list(map(int, input().split()))

cnt = 0
a_dict = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        a_dict[sum(a_arr[i:j+1])] += 1

for i in range(m):
    for j in range(i, m):
        cnt += a_dict[t - sum(b_arr[i:j+1])]

print(cnt)
