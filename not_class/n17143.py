'''
17143번: 낚시왕 / gold 1 / 구현, 시뮬레이션
'''
import sys

input = sys.stdin.readline


def move(shark):
    move_cnt = shark[2]
    dir = shark[3]
    nx, ny = shark[0], shark[1]
    # 움직이는 횟수에서 사이클 지워주기
    if dir == 1 or dir == 2:
        cycle = 2 * R - 2
    else:
        cycle = 2 * C - 2
    move_cnt = move_cnt % cycle
    if dir == 1:
        nx = shark[0] - move_cnt
        if nx < 1:
            nx = 1 + (abs(nx) + 1)
            dir = 2
            if nx > R:
                nx = R - (nx - R)
                dir = 1
    elif dir == 2:
        nx = shark[0] + move_cnt
        if nx > R:
            nx = R - (nx - R)
            dir = 1
            if nx < 1:
                nx = 1 + (abs(nx) + 1)
                dir = 2
    elif dir == 3:
        ny = shark[1] + move_cnt
        if ny > C:
            ny = C - (ny - C)
            dir = 4
            if ny < 1:
                ny = 1 + (abs(ny) + 1)
                dir = 3
    elif dir == 4:
        ny = shark[1] - move_cnt
        if ny < 1:
            ny = 1 + (abs(ny) + 1)
            dir = 3
            if ny > C:
                ny = C - (ny - C)
                dir = 4
    return nx, ny, dir


# 1. R, C, M, 상어정보 입력 받기
R, C, M = map(int, input().split())
shark = []
for i in range(M):
    shark.append(list(map(int, input().split())))

all_fishing = 0
# 한 칸씩 위치 이동
for col in range(1, C + 1):
    # (1) col와 같은 위치이면서 땅과 가장 가까운 상어 잡기
    top_shark = -1
    top_value = 1000
    # (1-1) 같은 위치의 땅과 가까운 상어 고르기
    for i in range(len(shark)):
        if shark[i][1] == col:
            if shark[i][0] < top_value:
                top_shark = i
                top_value = shark[i][0]
    # (1-2) 땅과 가장 가까운 상어 잡기
    if top_shark != -1:
        fishing_shark = shark.pop(top_shark)
        all_fishing += fishing_shark[-1]
    # (2) 상어 움직이기
    move_info = set()
    i = 0
    while i < len(shark):
        # i 상어 움직이기
        shark[i][0], shark[i][1], shark[i][3] = move(shark[i])
        # 겹치는게 있을 시,
        if (shark[i][0], shark[i][1]) in move_info:
            find = i - 1
            for pre in range(find, -1, -1):
                if shark[i][0] == shark[pre][0] and shark[i][1] == shark[pre][
                        1]:
                    if shark[i][-1] > shark[pre][-1]:
                        shark.pop(pre)
                    else:
                        shark.pop(i)
                    break
        # 겹치는게 없을 시,
        else:
            move_info.add((shark[i][0], shark[i][1]))
            i += 1

print(all_fishing)
