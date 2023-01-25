'''
2512 - 예산 / silver 3 / 이분탐색
'''
import sys
import copy

input = sys.stdin.readline

n = int(input())
city = list(map(int, input().split()))
m = int(input())

# 모든 요청이 배정될 수 있는 경우
if sum(city) <= m:
    print(max(city))
# 없는 경우
else:
    city.sort()
    res = 0
    start = m // n
    end = max(city)
    while start <= end:
        mid = (start + end) // 2
        check_city = copy.deepcopy(city)
        for i in range(len(city)):
            if check_city[i] > mid:
                check_city[i] = mid
        if sum(check_city) > m:
            end = mid - 1
        elif sum(check_city) < m:
            if res < mid:
                res = mid
            start = mid + 1
        else:
            res = mid
            break
    print(res)
