"""
5430 - AC (G5)
"""

from collections import deque


def input_que(que, arr):
    i = 0
    while i < len(arr):
        if arr[i] == "[" or arr[i] == "]" or arr[i] == ",":
            i += 1
        else:
            value = 0
            while arr[i] != "," and arr[i] != "]":
                value = 10 * value + int(arr[i])
                i += 1
            que.append(value)


def print_que(que):
    print("[", end="")
    i = 0
    while i < len(que):
        if i + 1 == len(que):
            print(que[i], end="")
        else:
            print(que[i], end=",")
        i += 1
    print("]")


# 1. 입력 받기
T = int(input())
for _ in range(T):
    command = input()
    arr_count = int(input())
    arr = input()
    que = deque()
    flag = True
    rev = 0

    # 2. 입력받은 arr를 que에 넣기
    input_que(que, arr)

    # 3. 입력받은 command 하나씩 처리
    for i in range(len(command)):
        if command[i] == "R":
            rev += 1
        elif command[i] == "D":
            if not que:
                flag = False
                print("error")
                break
            else:
                if rev % 2 == 0:
                    que.popleft()
                else:
                    que.pop()

    # 4. que에 값이 남아있으면, 형식에 맞게 출력
    if flag == True:
        if rev % 2 == 0:
            print_que(que)
        else:
            que.reverse()
            print_que(que)
    # 5. que 초기화
    que.clear()
