'''
17406번: 배열 돌리기 4 / gold 4 / 브루트포스
'''
import sys
import itertools
import copy
from collections import deque

input = sys.stdin.readline


def rotate_arr(tmp, r, c, s):
    point = [r - s - 1, c - s - 1, r + s - 1, c + s - 1]
    for _ in range(s):
        value = deque()
        x = point[0]
        # 오른쪽
        for col in range(point[1], point[3] + 1):
            value.append(tmp[x][col])
            if len(value) == 2:
                tmp[x][col] = value.popleft()
        y = point[3]
        # 아래
        for row in range(point[0] + 1, point[2] + 1):
            value.append(tmp[row][y])
            if len(value) == 2:
                tmp[row][y] = value.popleft()
        # 왼
        x = point[2]
        for col in range(point[3] - 1, point[1] - 1, -1):
            value.append(tmp[x][col])
            if len(value) == 2:
                tmp[x][col] = value.popleft()
        y = point[1]
        # 위
        for row in range(point[2] - 1, point[0] - 1, -1):
            value.append(tmp[row][y])
            if len(value) == 2:
                tmp[row][y] = value.popleft()
        for i in range(4):
            if i == 0 or i == 1:
                point[i] += 1
            else:
                point[i] -= 1


# 입력받기
N, M, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
rotate_oper = []
for _ in range(K):
    rotate_oper.append(list(map(int, input().split())))
# 회전 연산 정보 순서 경우의 수 만들기
case_index = [i for i in range(K)]
all_case = itertools.permutations(case_index, K)
# 최솟값 구하기
min_res = int(1e90)
for case in all_case:
    tmp = copy.deepcopy(arr)
    for index in case:
        r, c, s = rotate_oper[index]
        # 회전시키기
        rotate_arr(tmp, r, c, s)
    # 결과 확인
    for i in tmp:
        if sum(i) < min_res:
            min_res = sum(i)
print(min_res)
