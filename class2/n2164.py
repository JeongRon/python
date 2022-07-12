"""
2164 - 카드2 (silver 4)
"""
import sys
import collections

input = sys.stdin.readline

N = int(input())
N_deq = collections.deque([i for i in range(1, N + 1)])
while len(N_deq) != 1:
    N_deq.popleft()
    temp = N_deq[0]
    N_deq.popleft()
    N_deq.append(temp)

print(N_deq[0])

# 첫번째 인덱스를 pop을 하면, 시간복잡도 커짐
# deque(덱) 사용?!
# review
# 참고 : (https://wellsw.tistory.com/122) (https://excelsior-cjh.tistory.com/96)
# 덱 활용 기본 문제
# 덱이란? 리스트와 다른 점? 시간복잡도 차이 이해하기
