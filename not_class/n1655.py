'''
1655번 - 가운데를 말해요 / gold 2 / 우선순위 큐
'''
import sys
import heapq

input = sys.stdin.readline

n = int(input())
# left : 최소 힙 / right : 최대 힙
left = []
right = []

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 1:
        heapq.heappush(right, (-num, num))
    else:
        heapq.heappush(left, (num, num))

    if len(left) > 0 and right[0][1] > left[0][1]:
        left_num = heapq.heappop(left)[1]
        right_num = heapq.heappop(right)[1]
        heapq.heappush(left, (right_num, right_num))
        heapq.heappush(right, (-left_num, left_num))

    print(right[0][1])
