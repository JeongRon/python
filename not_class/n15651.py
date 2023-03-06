'''
15651번: N과 M (3) / silver 3 / itertools
'''
import itertools

# 1. 입력 받기 / n, m
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]
# 2. 중복 순열 리스트 만들기
permutation = list(itertools.product(arr, repeat=m))
# 3. 출력
for i in range(len(permutation)):
    tmp = permutation[i]
    for i in tmp:
        print(i, end=' ')
    print()
