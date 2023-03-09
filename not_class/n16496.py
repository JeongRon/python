'''
16496번: 큰 수 만들기 / platinum 5 / 그리디, 정렬
'''
import sys

input = sys.stdin.readline


def find_big(find_list):
    visited = [False for _ in range(len(find_list))]
    while True:
        big_index = -1
        for index in range(len(find_list)):
            if visited[index] == True:
                continue
            if big_index == -1:
                big_index = index
                continue
            tmp = int(find_list[index] + find_list[big_index])
            if tmp > int(find_list[big_index] + find_list[index]):
                big_index = index
        if big_index == -1:
            break
        else:
            visited[big_index] = True
            print(find_list[big_index], end='')


# 1. 입력 받기
n = int(input())
arr = list(map(str, input().split()))
# 2. 맨 앞자리 분류 하기
first_num = [[] for _ in range(10)]
for s in arr:
    index = int(s[0])
    first_num[index].append(s)
# 3. 0만 있을 시 예외처리
step = False
for i in range(1, 10):
    if len(first_num[i]) != 0:
        step = True
# 4. 맨 앞자리 똑같을 시 분류 하기
if step:
    for i in range(9, -1, -1):
        if len(first_num[i]) != 0:
            find_big(first_num[i])
else:
    print(0)
