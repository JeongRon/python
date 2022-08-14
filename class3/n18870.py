'''
18870 - 좌표 압축 (silver 2)
'''
import sys

input = sys.stdin.readline

N = int(input().rstrip())
input_lst = list(map(int, input().split()))
sorted_lst = sorted(list(set(input_lst)))
dic = {sorted_lst[i] : i for i in range(len(sorted_lst))}

for i in input_lst:
    print(dic[i], end=' ')