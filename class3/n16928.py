"""
16928 - 뱀과 사다리 게임 (G5)
"""
import sys
from collections import deque

input = sys.stdin.readline

# 1. Input
ladder, snake = map(int, input().split())
cross_from = []
cross_to = []
for _ in range(ladder + snake):
    x, y = map(int, input().split())
    cross_from.append(x)
    cross_to.append(y)
# 2. 0 ~ 100 번 인덱스까지 board 리스트 생성 / que 리스트 생성
board = [0 for _ in range(101)]
que = deque()

# 3. BFS / que에 넣을 값 : (1.인덱스(위치), 2.value(최단경로 값))
que.append((1, 0))
while que:
    location, value = que.popleft()
    for i in range(1, 7):
        move_location = location + i
        if move_location in cross_from:
            index = cross_from.index(move_location)
            move_location = cross_to[index]
        if move_location <= 100:
            move_value = value + 1
            if board[move_location] == 0:
                board[move_location] = move_value
                que.append((move_location, move_value))
            else:
                if board[move_location] > move_value:
                    board[move_location] = move_value
                    que.append((move_location, move_value))

print(board[100])
