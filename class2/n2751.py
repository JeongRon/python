"""
2751 - 수 정렬하기 2 (silver 5)
"""
import sys

N = int(sys.stdin.readline())
num = []
for i in range(N):
    num.append(int(sys.stdin.readline().strip()))

set_num = set(num)
num = list(set_num)
num.sort()

# print("---------")
for i in num:
    print(i)


# review
# 오름차순으로 정렬 / sort()함수 활용
# 중복되는 수 없애기 위해 set 이용 후, 리스트에 넣기 -> sort 오름차순
