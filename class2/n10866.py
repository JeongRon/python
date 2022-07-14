"""
10866 - 덱 (silver 4)
"""
import sys
import collections

input = sys.stdin.readline

N = int(input())
deq = collections.deque([])

for _ in range(N):
    C = input().split()
    if C[0] == "push_front":
        C[1] = int(C[1])
        deq.appendleft(C[1])
    elif C[0] == "push_back":
        C[1] = int(C[1])
        deq.append(C[1])
    elif C[0] == "pop_front":
        if not deq:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()
    elif C[0] == "pop_back":
        if not deq:
            print(-1)
        else:
            print(deq[-1])
            deq.pop()
    elif C[0] == "size":
        print(len(deq))
    elif C[0] == "empty":
        if not deq:
            print(1)
        else:
            print(0)
    elif C[0] == "front":
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif C[0] == "back":
        if not deq:
            print(-1)
        else:
            print(deq[-1])

# review
# deque 덱 사용하기 연습 / 한번에 맞음!
