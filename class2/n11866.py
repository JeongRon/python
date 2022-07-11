"""
11866 - 요세푸스 문제 0 (silver 5)
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

josephus_list = [i for i in range(1, N + 1)]

print_list = []
pop = 0

for i in range(N - 1, -1, -1):
    pop += K - 1
    while pop > i:
        pop = pop - i - 1
    temp = josephus_list[pop]
    print_list.append(temp)
    josephus_list.pop(pop)

print("<", end="")
for i in range(N):
    if i == N - 1:
        print(print_list[i], end="")
    else:
        print(print_list[i], end=", ")
print(">", end="")

"""
review
1. N 입력에 따른 요세푸스 리스트 생성
2. pop 변수는 pop할 인덱스 번호 나타냄 -> 규칙 찾기
3. 요세푸스 리스트를 pop하고, pop 한 값을 print 리스트에 추가
"""
