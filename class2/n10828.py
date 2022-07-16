"""
10828 - 스택 (silver 4)
"""
import sys

input = sys.stdin.readline

N = int(input())
stack_lst = []

for _ in range(N):
    C = input().split()
    if C[0] == "push":
        C[1] = int(C[1])
        stack_lst.append(C[1])
    elif C[0] == "pop":
        if not stack_lst:
            print(-1)
        else:
            print(stack_lst[-1])
            stack_lst.pop()
    elif C[0] == "size":
        print(len(stack_lst))
    elif C[0] == "empty":
        if not stack_lst:
            print(1)
        else:
            print(0)
    elif C[0] == "top":
        if not stack_lst:
            print(-1)
        else:
            print(stack_lst[-1])

# review - 한번에 통과
# 덱을 안만들어도 append, pop 이용가능
# 시간 복잡도 이해 append, pop
