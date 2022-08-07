"""
1541 - 잃어버린 괄호 (silver 2)
"""
import sys
import re

input = sys.stdin.readline

expression = input().rstrip()
num = re.split("[+|-]", expression)
sign = [None]
for i in expression:
    if i == "-" or i == "+":
        sign.append(i)

for i in range(len(sign)):
    if sign[i] == "+":
        if sign[i - 1] == "-":
            sign[i] = "-"

# print(num)
# print(sign)

result = 0
for i in range(len(num)):
    num[i] = int(num[i])
    if sign[i] == "-":
        num[i] = -1 * num[i]
    result += num[i]

print(result)
