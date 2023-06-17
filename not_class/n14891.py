'''
14891번: 톱니바퀴 / gold 5 / 구현, 시뮬레이션
'''
import sys
from collections import deque

input = sys.stdin.readline

# 톱니바퀴 입력받기
graph = deque()
for i in range(4):
    case = deque(input().rstrip())
    graph.append(case)
# 회전 입력받기
move = []
# 시뮬레이션
K = int(input())
for _ in range(K):
    move_num, move_dir = map(int, input().split())
    move_num -= 1
    move_dir_rev = move_dir * -1
    move_graph = []
    move_graph.append((move_num, move_dir))
    # 움직일 톱니바퀴의 왼쪽 체크
    for i in range(move_num - 1, -1, -1):
        if graph[i][2] != graph[i + 1][6]:
            move_graph.append((i, move_dir_rev))
            move_dir_rev *= -1
        else:
            break
    # 움직일 톱니바퀴의 오른쪽 체크
    move_dir_rev = move_dir * -1
    for i in range(move_num + 1, 4):
        if graph[i - 1][2] != graph[i][6]:
            move_graph.append((i, move_dir_rev))
            move_dir_rev *= -1
        else:
            break
    # 톱니바퀴 움직이기 
    for index, dir in move_graph:
        if dir == 1:
            graph[index].appendleft(graph[index].pop())
        else:
            graph[index].append(graph[index].popleft())
# 결과값 출력하기
res = 0
point = [1, 2, 4, 8]
for i in range(4):
    if graph[i][0] == '1':
        res += point[i]
print(res)
