'''
10819번: 차이를 최대로 / silver 2 / 브루트포스, 순열
'''
import itertools
# N, arr 입력받기
N = int(input())
arr = list(map(int, input().split()))
# 순열 활용 case_arr 만들기
case_arr = itertools.permutations(arr, N)
# 최대값 구하기
max_res = 0
# case_arr 에서 하나씩 꺼내어 case의 최대값을 구한뒤, 전체 최대값과 비교 
for case in case_arr:
    res = 0
    for i in range(1, len(case)):
        res += abs(case[i - 1] - case[i])
    if max_res < res:
        max_res = res
# 최대값 출력하기
print(max_res)
