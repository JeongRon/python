"""
우선순위 큐 / 최소 힙(Min Heap)

- 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
- 표준 라이브러리 형태로 지원 (import heapq)

- 우선순위 큐 구현 방식 
(삽입시간 - 리스트:O(1), 힙:O(logN))
(삭제시간 - 리스트:O(N), 힙:O(logN))
- 즉, 리스트에서 값을 삽입 삭제 하는 것보다 빠르다
- 원하는 값을 찾는 시간도 없어짐
  (가장 작은 값, 가장 큰 값 힙의 첫번째 인덱스에 있도록 함)
"""

import heapq

# 오름차순 힙 정렬 (Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
