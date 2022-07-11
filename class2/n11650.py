"""
11650 - 좌표 정렬하기 (silver 5)
"""
import sys

input = sys.stdin.readline
N = int(input())
location_list = []
for i in range(N):
    location = tuple(map(int, input().split()))
    location_list.append(location)

location_list.sort(key=lambda x: x[1])
location_list.sort(key=lambda x: x[0])

for i in range(N):
    print(location_list[i][0], location_list[i][1])

"""
review
- input = sys.stdin.readline 설정하기 배움
- sort로 분류하기 
    - key 를 lambda를 활용해서 원하는 결과 도출
"""
