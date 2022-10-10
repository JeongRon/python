"""
10807 - 개수 세기 (B5)
"""

N = int(input())
arr = list(map(int, input().split()))
find_num = int(input())
count = 0
for i in arr:
    if i == find_num:
        count += 1
print(count)
