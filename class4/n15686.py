"""
15686 - 치킨 배달 / gold 5 / 브루트포스, itertools
"""
import sys
import itertools

input = sys.stdin.readline

# n: n*n 지도 / m: 폐업 후 치킨집
n, m = map(int, input().split())

# array / 0: 빈 칸, 1: 집, 2: 치킨집
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 집, 치킨집 위치 넣기
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            house.append((i, j))
        elif array[i][j] == 2:
            chicken.append((i, j))
            array[i][j] = 0

# 치킨집 case
case = list(itertools.combinations(chicken, m))


# m개의 치킨집 위치가 들어있는 case에서 나올 수 있는 최소거리 구하는 함수
def one_case_result(arr, house, case):
    all_distance = 0
    for row, col in house:
        one_distance = 1000
        for a, b in case:
            dist = abs(row - a) + abs(col - b)
            if one_distance > dist:
                one_distance = dist
        all_distance += one_distance
    return all_distance


# 치킨집 case를 모두 탐색 후, 가장 작은 결과 값 all_min_result에 넣기
all_min_result = 100000
for one_case in case:
    one_result = one_case_result(array, house, one_case)
    if one_result < all_min_result:
        all_min_result = one_result

print(all_min_result)
