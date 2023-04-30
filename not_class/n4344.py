'''
4344번: 평균은 넘겠지 / bronze 1 / 수학
'''
import sys

input = sys.stdin.readline

C = int(input())
for _ in range(C):
    student = list(map(int, input().split()))
    average = 0
    for i in range(1, len(student)):
        average += student[i]
    average /= student[0]
    aboveAverageStudent = 0
    for i in range(1, len(student)):
        if average < student[i]:
            aboveAverageStudent += 1
    aboveAverageStudent /= student[0]
    aboveAverageStudent *= 100
    print(f"{aboveAverageStudent:.3f}%")
