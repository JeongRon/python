'''
15649번 - N과 M (1) / silver 3 / itertools
'''
import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
perm = list(itertools.permutations(arr, m))

for i in range(len(perm)):
    for j in range(m):
        print(perm[i][j], end=' ')
    print()
