'''
17135번: 캐슬 디펜스 / gold 3 / 조합, copy, 시뮬레이션
'''
import sys
import itertools
import copy

input = sys.stdin.readline


def simulation(case, enemy):
    count = 0
    visited = [False for _ in range(len(enemy))]
    visited_cnt = 0
    while True:
        # 종료조건
        if len(enemy) == visited_cnt:
            break
        # 궁수 3명이 공격할 적 attack 세트에 담기
        attack = set()
        # 궁수 한명씩 뽑기 / x,y 좌표
        for y in case:
            x = N
            # 가까운 적 찾기
            close = [100, -1, -1, -1]
            for i in range(len(enemy)):
                # 뽑은 적이 이미 없어졌으면 pass / 있으면 궁수와 적의 거리 확인 후 가까운 적 등록
                if not visited[i]:
                    # 적 위치 좌표 a,b
                    a, b = enemy[i][0], enemy[i][1]
                    # 현재 궁수 x,y 와 적 a,b 좌표 사이 거리 구하기
                    dist = abs(a - x) + abs(b - y)
                    if dist <= D:
                        if dist < close[0]:
                            close[0] = dist
                            close[1] = i
                            close[2] = a
                            close[3] = b
                        elif dist == close[0] and close[3] > b:
                            close[0] = dist
                            close[1] = i
                            close[2] = a
                            close[3] = b
            # 한 궁수가 공격할 수 있는 적이 없을 시 pass / 있을 시 attack 세트에 추가하기
            if close[0] != 100:
                attack.add((close[1], close[2], close[3]))
        # attack 세트에 담아둔 적들 제거하기
        for i, a, b in attack:
            visited[i] = True
            visited_cnt += 1
            # 궁수에 의해 제거된 적 count
            count += 1
        # 적(enemy) 한 칸 밑으로 움직이기
        for i in range(len(enemy)):
            if not visited[i]:
                enemy[i][0] += 1
                # 성에 도착한 적들 없애기
                if enemy[i][0] == N:
                    visited[i] = True
                    visited_cnt += 1
    return count


# N, M, D, graph 입력
N, M, D = map(int, input().split())
graph = []
# graph에서 적의 위치 all_enemy 리스트에 저장
all_enemy = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            all_enemy.append([i, j])
# 조합을 이용한 궁수 배치 경우의 수 all_case에 담기
tmp = [i for i in range(M)]
all_case = itertools.combinations(tmp, 3)
# 궁수 배치 경우의 수를 하나씩 꺼내서 적 제거 확인하기
max_cnt = 0
for case in all_case:
    # 턴마다 적의 위치가 바뀌므로 deepcopy로 복사해서 사용
    enemy = copy.deepcopy(all_enemy)
    cnt = simulation(case, enemy)
    if max_cnt < cnt:
        max_cnt = cnt
# 최대 적 제거 출력하기
print(max_cnt)
