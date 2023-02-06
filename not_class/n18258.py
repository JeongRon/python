'''
18258번 - 큐 2 / silver4 / deque
'''
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = deque()
for _ in range(n):
    command = input().rstrip()
    if command == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif command == 'size':
        print(len(arr))
    elif command == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif command == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    else:
        # push 일때,
        num = int(command[5:])
        arr.append(num)
