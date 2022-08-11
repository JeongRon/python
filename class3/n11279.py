"""
11279 - 최대 힙 (silver 2) 
"""
import sys
import heapq

input = sys.stdin.readline

heap_list = []
n = int(input().rstrip())
for _ in range(n):
    x = int(input().rstrip())
    if x == 0:
        if not heap_list:
            print("0")
        else:
            print(heapq.heappop(heap_list)[1])
    else:
        heapq.heappush(heap_list, (-x, x))
