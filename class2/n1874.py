"""
1874 - 스택 수열 (siver 2)
"""
import sys

input = sys.stdin.readline


n = int(input())
count = 0
stack = []
result = []
is_seq = True

for _ in range(n):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        is_seq = False


if is_seq:
    print("\n".join(result))
else:
    print("NO")

# review - 시간초과 3번 / 구현만 성공
# 참고 (https://assaeunji.github.io/python/2020-05-04-bj1874/)
# 입력 받은 수열 바로 처리 하도록 코드 작성 중요

# <<< 내가 작성한 코드 >>>
# seq_list = []
# stack_list = []
# temp_list = []

# n = int(input())
# for _ in range(n):
#     seq_list.append(int(input()))

# num = 1
# index = 0
# is_seq = True
# while index < n:
#     if seq_list[index] not in temp_list:
#         temp_list.append(num)
#         stack_list.append("+")
#         num += 1
#     elif seq_list[index] == temp_list[-1]:
#         temp_list.pop()
#         stack_list.append("-")
#         index += 1
#     else:
#         is_seq = False
#         print("No")
#         break
# if is_seq:
#     for i in stack_list:
#         print(i)
