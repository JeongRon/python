"""
7662 - 이중 우선순위 큐 (G4)
"""
import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    K = int(input().rstrip())
    min_heap = []
    max_heap = []
    visited = [False for _ in range(K)]
    for key in range(K):
        command, number = input().split()
        number = int(number)

        if command == "I":
            heapq.heappush(min_heap, (number, key))
            heapq.heappush(max_heap, (-number, key))
            visited[key] = True
        elif command == "D":
            if number == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif number == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
