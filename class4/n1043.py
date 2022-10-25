"""
1043 - 거짓말 / gold 4 / set 활용
"""
import sys

input = sys.stdin.readline

# 1. Input
n, m = map(int, input().split())
true_list = list(map(int, input().split()))
true_set = set(true_list[1:])

party_list = []
for _ in range(m):
    party_info = list(map(int, input().split()))
    party_list.append(set(party_info[1:]))

# 2. ture_set / add
for _ in range(m):
    for party_set in party_list:
        if party_set & true_set:
            true_set = true_set.union(party_set)

# 3. count
count = 0
for party_set in party_list:
    if party_set & true_set:
        continue
    count += 1

print(count)
