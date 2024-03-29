"""
우선순위 큐 / 최대 힙(Max Heap)

- 기본 heapq 표준 라이브러리는 최소 힙

- 마이너스(-)를 활용해서 최대 힙으로 변환 및 활용
"""
import heapq

# 내림차순 힙 정렬 (Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
