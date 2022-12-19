'''
20309번 - 트리플 소트 / silver 3
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

flag = True
for i in range(n - 1):
    num = arr[i]
    if num % 2 == 0:
        if i % 2 == 0:
            flag = False
            break
    else:
        if i % 2 == 1:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')
