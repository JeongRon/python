"""
11723 - 집합 (silver 5)
"""
import sys

input = sys.stdin.readline

S = set()

n = int(input())
for _ in range(n):
    cmd = input().split()

    if len(cmd) == 2:
        cmd[1] = int(cmd[1])

    if cmd[0] == "add":
        S.add(cmd[1])
    elif cmd[0] == "remove":
        S.discard(cmd[1])
    elif cmd[0] == "check":
        if S.isdisjoint({cmd[1]}):
            print(0)
        else:
            print(1)
    elif cmd[0] == "toggle":
        if S.isdisjoint({cmd[1]}):
            S.add(cmd[1])
        else:
            S.remove(cmd[1])
    elif cmd[0] == "all":
        S = set(range(1, 21))
    elif cmd[0] == "empty":
        S.clear()

# review
# 리스트를 쓸까 고민하다, 해당 문제에서 요소 순서가 상관으므로 SET 사용
# 세트에서의 추가 삭제 초기화 값체크 등의 함수들 한번 사용해 봄
