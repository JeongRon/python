"""
1676 - 팩토리얼 0의 개수 (silver 5)
"""
import sys

input = sys.stdin.readline

N = int(input())

fac = 1
cnt = 0

for i in range(1, N + 1):
    fac *= i

while True:
    if fac % 10 == 0:
        cnt += 1
        fac //= 10
    else:
        break
print(cnt)

# review
# 문제를 잘못 읽어서 팩토리얼 값에서 모든 0을 구하도록 코드를 짰었음
# 맨 뒤 일의자리 부터 0이 연속적으로 나오는 것만 count하는 문제
