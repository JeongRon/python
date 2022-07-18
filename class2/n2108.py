"""
2108 - 통계학 (silver 3)
"""
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(int(input()))
lst.sort()

# print("-------------")
# print(lst)

# 1. 산술평균
avg = sum(lst) / len(lst)
print(round(avg))

# 2. 중앙값
print(lst[N // 2])

# 3. 최빈값
lst_counter = Counter(lst).most_common(2)

if len(lst_counter) == 2 and lst_counter[0][1] == lst_counter[1][1]:
    print(lst_counter[1][0])
else:
    print(lst_counter[0][0])

# 4. 범위
print(len(range(lst[0], lst[-1])))

# review
# 1. round() 반올림 함수 활용 / 참고 (https://dpdpwl.tistory.com/94)
# 2. Counter 클래스 + most_common(2) 함수 활용 / 참고 (https://dongdongfather.tistory.com/70)
# 필요한 함수를 활용하여 문제 풀이
