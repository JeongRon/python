'''
20055번: 컨베이어 벨트 위의 로봇 / gold 5 / 시뮬레이션
'''
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
convey = list(map(int, input().split()))
convey = deque(convey)
robot = [0 for _ in range(N)]
robot = deque(robot)

res = 0
done = 0
# 로봇 옮기는 과정 시뮬레이션 실행
while True:
    res += 1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    convey.appendleft(convey.pop())
    robot.appendleft(0)
    robot.pop()
    if robot[-1] == 1:
        robot[-1] = 0
    # 2. 로봇 한 칸 이동
    for i in range(N - 1, -1, -1):
        if robot[i] == 1:
            # 옆에 컨베이어 내구성 있고, 로봇이 없을 시,
            if robot[i + 1] == 0 and convey[i + 1] > 0:
                robot[i], robot[i + 1] = 0, 1
                convey[i + 1] -= 1
                if convey[i + 1] == 0:
                    done += 1
    # 3. 올리는 위치에 로봇 올리기
    if convey[0] != 0:
        robot[0] = 1
        convey[0] -= 1
        if convey[0] == 0:
            done += 1
    # 4. 내구도 0인 컨베이어 칸 K개 이상인지 확인
    if done >= K:
        break
# 출력하기
print(res)
