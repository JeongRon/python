"""
10989 - 수 정렬하기 3 (bronze 1)
"""
import sys

N = int(sys.stdin.readline())
num_list = [0] * 10001
for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

# 실패 - 메모리 초과
# append로 입력한 숫자 인덱스에 넣기
# sorted함수로 오름차순 인덱스

# 성공
# 1. 입력 input() / sys.stdin.readline()
# 2. num_list 리스트를 만들고 인덱스를 10,001 크기만큼 지정
# 해당 인덱스 번호는 숫자를 의미하고, 해당 인덱스의 값은 해당 숫자가 얼만큼 나왔는지를 의미
