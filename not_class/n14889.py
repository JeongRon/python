'''
14889번: 스타트와 링크 / silver 2 / 브루트포스
'''
import sys
import itertools

input = sys.stdin.readline


def set_point(team):
    point = 0
    for i in team:
        for j in team:
            point += graph[i][j]
    return point


# 전체 몇명인지 n, 시너지 효과 graph
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 경우의 수 만들기
numb = [i for i in range(n)]
comb = list(itertools.combinations(numb, n // 2))
# 최솟값 담을 변수 min_gap
min_gap = int(1e9)
# 만든 경우의 수를 하나씩 꺼내기
for i in comb:
    # start, link 팀 선수 분류 하기
    start_team = list(i)
    link_team = list(set(numb) - set(start_team))
    # 분류한 팀의 능력치 총합 구하기
    start_point = set_point(start_team)
    link_point = set_point(link_team)
    # 최솟값인지 확인하기
    gap = abs(start_point - link_point)
    if gap < min_gap:
        min_gap = gap
        if min_gap == 0:
            break
# 결과 출력
print(min_gap)
