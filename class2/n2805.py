"""
2805 - 나무 자르기 (silver 2)
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

tree_list = list(map(int, input().split()))

H_start = 0
H_end = max(tree_list)

while H_start <= H_end:
    cut_tree = 0
    H_mid = (H_start + H_end) // 2

    for tree in tree_list:
        if tree > H_mid:
            cut_tree += tree - H_mid

    if cut_tree >= M:
        H_start = H_mid + 1
    else:
        H_end = H_mid - 1
print(H_end)

# review
# 이분 탐색 알고리즘
