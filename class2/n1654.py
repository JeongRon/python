"""
1654 - 랜선 자르기 (silver 2)
"""
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lst = []
for _ in range(K):
    lst.append(int(input()))

start, end = 1, max(lst)
print(end)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in lst:
        count += i // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
# <<< 내가 처음 푼 코드 >>>
# K, N = map(int, input().split())
# lst = []
# for _ in range(K):
#     lst.append(int(input()))

# long = sum(lst) // N

# while True:
#     count = 0
#     for i in lst:
#         count += i // long
#     if count == N:
#         break
#     long -= 1
# print(long)
