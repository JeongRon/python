"""
9935 - 문자열 폭발 / gold 4 / 문자열, 스택
"""
from collections import deque

arr = list(input())
rm = list(input())
arr_len = len(arr)
rm_len = len(rm)

stack = deque()

for i in range(arr_len):
    stack.append(arr[i])
    if stack[-1] == rm[-1] and len(stack) >= rm_len:
        temp = [stack[i] for i in range(-rm_len, 0)]
        if temp == rm:
            for _ in range(rm_len):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
