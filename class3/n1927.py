"""
1927 - 최소 힙 (silver 2)
"""
import sys
import heapq

input = sys.stdin.readline

heap = []
n = int(input().rstrip())

for _ in range(n):
    x = int(input().rstrip())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
