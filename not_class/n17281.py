'''
17281번: ⚾ / gold 4 / 구현, 브루트포스
'''
import sys
import itertools

input = sys.stdin.readline

# 입력받기
N = int(input())
baseBallScore = []
for _ in range(N):
    baseBallScore.append(list(map(int, input().split())))
# 경우의 수 만들기
arr = [i for i in range(1, 9)]
allCase = itertools.permutations(arr, len(arr))
# 시뮬레이션
maxScore = 0
for case in allCase:
    case = list(case)
    case.insert(3, 0)
    nowOrder = 0
    score = 0
    for round in baseBallScore:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if round[case[nowOrder]] == 0:
                out += 1
            elif round[case[nowOrder]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif round[case[nowOrder]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif round[case[nowOrder]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif round[case[nowOrder]] == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            nowOrder = (nowOrder + 1) % 9
    if maxScore < score:
        maxScore = score

print(maxScore)
