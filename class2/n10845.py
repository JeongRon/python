"""
10845 - 큐 (silver 4)
"""
import sys
from collections import deque

input = sys.stdin.readline

que = deque()
N = int(input())

for _ in range(N):
    C = input().split()

    if C[0] == "push":
        C[1] = int(C[1])
        que.append(C[1])
    elif C[0] == "pop":
        if not que:
            print(-1)
        else:
            print(que[0])
            que.popleft()
    elif C[0] == "size":
        print(len(que))
    elif C[0] == "empty":
        if not que:
            print(1)
        else:
            print(0)
    elif C[0] == "front":
        if not que:
            print(-1)
        else:
            print(que[0])
    elif C[0] == "back":
        if not que:
            print(-1)
        else:
            print(que[-1])

# review (한번에 맞음!)
# 참고 / 파이썬 큐 사용 3가지 방법 (https://www.daleseo.com/python-queue/)
# 1. pop(0) / 2. deque를 활용 / 3. queue 활용
# 큐란? 선입선출 / 값을 넣을 때 뒤로 + 값을 뺄때는 앞으로
