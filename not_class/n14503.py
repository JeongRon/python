'''
14503번: 로봇 청소기 / gold 5 / 구현-시뮬레이션
'''
import sys

input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 현재 방향 d일때, 뒤로 - 남, 서, 북, 동
back_dx = [1, 0, -1, 0]
back_dy = [0, -1, 0, 1]
# 현재 방향 d일때, 앞으로 - 북, 동, 남, 서
front_dx = [-1, 0, 1, 0]
front_dy = [0, 1, 0, -1]

count = 0
while True:
    # 1-1. 현재 칸 빈 칸이면, count 1 증가
    if graph[r][c] == 0:
        count += 1
    # 1-2. 현재 칸 청소 하기 / -1 표시
    graph[r][c] = -1
    # 2. 현재 칸의 주변 4칸, 청소되지 않은 빈 칸 확인 하기
    possible_direction = 0
    for i in range(4):
        nx, ny = r + back_dx[i], c + back_dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 0:
                possible_direction += 1
    # 3-1. 주변 4칸이 모두 청소되어 있을 시, 현재 방향에서 후진
    if possible_direction == 0:
        nx, ny = r + back_dx[d], c + back_dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                break
            else:
                r, c = nx, ny
        else:
            break
    # 3-2. 주변 4칸 중 청소되지 않은 빈 칸 있을 시, 반시계방향 90도회전 + 바라보는방향 앞쪽 빈 칸 확인
    else:
        for i in range(1, 5):
            tmp_d = d - i
            if tmp_d < 0:
                tmp_d += 4
            nx, ny = r + front_dx[tmp_d], c + front_dy[tmp_d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    r, c = nx, ny
                    d = tmp_d
                    break
# count 출력
print(count)
