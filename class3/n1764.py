"""
1764 - 듣보잡 (silver 4)
"""
import sys

input = sys.stdin.readline

N_set = set()
M_set = set()
N, M = map(int, input().split())
for _ in range(N):
    N_set.add(input().rstrip())
for _ in range(M):
    M_set.add(input().rstrip())
NM_set = N_set & M_set
print(len(NM_set))
for i in sorted(NM_set):
    print(i)

# review
# 세트를 통해서 교집합 구하고, 출력
# 세트에서는 요소의 순서가 없지만, sorted로 값을 나열해서 출력 가능
