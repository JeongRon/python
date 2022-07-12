"""
1920 - 수 찾기 (silver 4)
"""
import sys

input = sys.stdin.readline

N = int(input())

A = set(map(int, input().split()))

M = int(input())

B = tuple(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)

# review
# 시간 초과 2번
# 참고 : https://chancoding.tistory.com/44
# 시간 복잡도 관련 개념을 알게 됨
# 리스트의 in연산자를 통한 포함 여부의 시간 복잡도는 O(N)
# 이분 탐색의 시간 복잡도는 O(logN)
# set과 Dictionary의 in연산을 통한 포함 여부 확인의 시간 복잡도는 O(1)
# 따라서 해당 집합 포함되는지만 확인하면 되므로 Set자료형 사용
