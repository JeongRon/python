"""
4949 - 균형잡힌 세상 (silver 4)
"""
import sys

input = sys.stdin.readline

while 1:
    S = input().rstrip()

    if S == ".":
        break

    stack = []
    is_balanced = 1

    for i in S:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                is_balanced = 0
                break
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_balanced = 0
                break

    if is_balanced and not stack:
        print("yes")
    else:
        print("no")
