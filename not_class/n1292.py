"""
1292 - 쉽게 푸는 문제
"""

A, B = map(int, input().split())

result = 0
num = 1
index = 0
while True:

    temp = num

    while temp != 0:
        index += 1
        if A <= index <= B:
            result += num
        temp -= 1

    if index > B:
        break

    num += 1

print(result)
