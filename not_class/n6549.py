'''
6549번: 히스토그램에서 가장 큰 직사각형 / platinum 5 / 스택, 구현
'''
import sys

input = sys.stdin.readline

while True:
    # 입력 받기
    info = list(map(int, input().split()))
    n = info.pop(0)
    # 종료 조건
    if n == 0:
        break
    # 가장 큰 직사각형 구하기
    stack = []
    big_area = 0
    for i in range(n):
        while len(stack) != 0 and info[stack[-1]] > info[i]:
            index = stack.pop()
            if len(stack) == 0:
                width = i
            else:
                width = i - 1 - stack[-1]
                area = width * info[index]
            big_area = max(big_area, area)
        stack.append(i)
    # 스택에 남아있는 부분
    while len(stack) != 0:
        index = stack.pop()
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        area = width * info[index]
        big_area = max(big_area, area)
    print(big_area)
