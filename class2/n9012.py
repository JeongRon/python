"""
9012 - 괄호 (silver 4)
"""
import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    S = input()

    S_list = []
    Correct = True

    for j in S:
        if j == "(":
            S_list.append(j)
        elif j == ")":
            if not S_list:
                Correct = False
                break
            elif S_list[-1] == "(":
                S_list.pop()

    if not S_list and Correct:
        print("YES")
    else:
        print("NO")
