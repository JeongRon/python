'''
13458번: 시험 감독 / bronze 2 / 수학
'''
import sys

input = sys.stdin.readline

N = int(input())
exam_room = list(map(int, input().split()))
monitoring = list(map(int, input().split()))
all_cnt = 0

for student in exam_room:
    cnt = 0
    # 총감독관 1명 투입
    student -= monitoring[0]
    cnt += 1
    # 부감독관 투입
    if student > 0:
        if student % monitoring[1] == 0:
            cnt += student // monitoring[1]
        else:
            cnt += int(student / monitoring[1]) + 1
    all_cnt += cnt
print(all_cnt)
