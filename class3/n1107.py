"""
1107 - 리모컨 (G5)
(1) move_channel : 이동하려는 채널 번호
(2) M : 고장난 번호 개수, borken_btn : 고장난 번호 리스트
"""
import sys

input = sys.stdin.readline

# 1. 입력 받기
move_channel = int(input())
M = int(input())
broken_btn = []
for _ in range(M):
    broken_btn = list(map(int, input().split()))
    break

# 이동하려는 채널이 100번이면, 현재 채널이 100번이므로 0 출력
if move_channel == 100:
    print(0)
else:
    # 현재 채널 / 이동할 채널 차이 result에 넣기
    result = abs(100 - move_channel)

    # 0 ~ 1000000 까지 모든 경우의 수 확인 (브루트포스)
    for num in range(1000001):
        num = str(num)
        flag = True
        # 고장난 번호를 가지고 있으면 바로 return
        for i in range(len(num)):
            if int(num[i]) in broken_btn:
                flag = False
                break
        # 고장난 번호 없는 num -> 현재 result와 비교해서 제일 작은 값 리셋
        if flag == True:
            step = len(num) + abs(int(num) - move_channel)
            result = min(result, step)
    print(result)
