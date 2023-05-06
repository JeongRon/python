'''
14499번: 주사위 굴리기 / gold 4 / 구현, 시뮬레이션
'''
import sys

input = sys.stdin.readline

# 입력 받기
N, M, x, y, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
command = list(map(int, input().split()))
# 주사위 [위, 아래, 동, 서, 남, 북]
dice = [0 for _ in range(6)]
# 명령어 (1,2,3,4) -> (x,y) 좌표 이동
dir = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
# 명령어 (1,2,3,4) -> 주사위 위치 변경
dice_dir = [[], [2, 3, 1, 0, 4, 5], [3, 2, 0, 1, 4, 5], [5, 4, 2, 3, 0, 1],
            [4, 5, 2, 3, 1, 0]]
# 명령어 하나씩 실행하기
for c in command:
    # 좌표 이동 확인
    if 0 <= x + dir[c][0] < N and 0 <= y + dir[c][1] < M:
        # 좌표 이동하기
        x += dir[c][0]
        y += dir[c][1]
        # 주사위 이동하기
        tmp = [0 for _ in range(6)]
        for i in range(6):
            tmp[i] = dice[dice_dir[c][i]]
        dice = tmp
        # 지도 칸 확인하기 / 0일 때, 0이 아닐 때
        if graph[x][y] == 0:
            graph[x][y] = dice[1]
        else:
            dice[1] = graph[x][y]
            graph[x][y] = 0
        # 현재 주사위 윗면 출력
        print(dice[0])
