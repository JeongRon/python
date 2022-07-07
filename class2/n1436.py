"""
1436 - 영화감독 숌 (silver 5)
"""
import sys

N = int(sys.stdin.readline())
movie = 666
count = 0

while True:
    if "666" in str(movie):
        count += 1
        # print(movie)
    if count == N:
        print(movie)
        break
    movie += 1

# review
# 1. 문제 이해 / '666'이 들어간 숫자 중에서 가장 작은 수를 순서대로 나열 한 것
# 2. 문자열 in 문자열 활용 /
