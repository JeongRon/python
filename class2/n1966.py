"""
1966 - 프린터 큐 (silver 3)
"""
import sys
import collections

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    que_list = collections.deque(map(int, input().split()))
    que_index = collections.deque(i for i in range(N))
    que_index[M] = "Print"

    count = 0
    while True:
        if que_list[0] == max(que_list):
            count += 1
            if que_index[0] == "Print":
                print(count)
                break
            else:
                que_list.popleft()
                que_index.popleft()
        else:
            que_list.append(que_list.popleft())
            que_index.append(que_index.popleft())

# review
# 처음에, 문제에 대한 이해가 잘 안되었음 (문제 요약) ->
# 리스트를 받고, 맨 처음 인덱스[0]가 우선순위(가장 큰 수)가 아니면 맨 뒤로 보내기
# 우선순위 이면 -> 프린트 할 인덱스이면 프린트 / 아니면 pop 지우기
#
# 중요 포인트
# 1. 리스트가 뒤로 보내거나 지우는 경우가 있기에
# 해당 인덱스 번호와 프린트 해야 할 인덱스를 나타내기 위한 que_index를 만들기
# 2. append(pop()) 코드 처음 사용해 봄
