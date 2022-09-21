from collections import deque

house_list = []
house_count = []
# 1. 입력 받기
N = int(input())
for _ in range(N):
    house_list.append(list(map(int, input())))


def house_check(x, y, flag):
    if house_list[x][y] == 0 or house_list[x][y] >= 2:
        return 0
    elif house_list[x][y] == 1:
        count = 1
        que = deque()
        house_list[x][y] = flag
        que.append((x, y))
        while que:
            pop_x, pop_y = que.popleft()
            for i in range(4):
                mv_x = pop_x + dx[i]
                mv_y = pop_y + dy[i]
                if mv_x < 0 or mv_x >= N or mv_y < 0 or mv_y >= N:
                    continue
                elif house_list[mv_x][mv_y] == 1:
                    house_list[mv_x][mv_y] = flag
                    count += 1
                    que.append((mv_x, mv_y))
        house_count.append(count)
        return 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = 2
for i in range(N):
    for j in range(N):
        if house_check(i, j, flag) == 1:
            flag += 1

print(len(house_count))
for i in sorted(house_count):
    print(i)
