'''
1715번 - 카드 정렬하기 / gold 4 / 우선순위 큐
'''
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    heapq.heappush(heap, num)

if len(heap) == 1:
    print(0)
else:
    res = 0
    while len(heap) > 1:
        new = heapq.heappop(heap) + heapq.heappop(heap)
        res += new
        heapq.heappush(heap, new)
    print(res)
