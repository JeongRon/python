'''
14888번: 연산자 끼워넣기 / silver 1 / 
'''
import sys
import itertools

input = sys.stdin.readline
# 1. 입력받기
n = int(input())
arr = list(map(int, input().split()))
op_cnt = list(map(int, input().split()))
# 2. op_list 만들기
operator = ['+', '-', '*', '//']
op_list = []
for i in range(4):
    for o in range(op_cnt[i]):
        op_list.append(operator[i])
# 3. op_case 만들기
op_case = itertools.permutations(op_list, n - 1)


# 4. min_res, max_res 구하기
def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '//':
        if a < 0:
            return (-a // b) * -1
        else:
            return a // b


res_case = []
for case in op_case:
    a, b = arr[0], arr[1]
    op = case[0]
    res = calculate(a, op, b)
    for i in range(1, len(case)):
        a = res
        b = arr[i + 1]
        op = case[i]
        res = calculate(a, op, b)
    res_case.append(res)
# 5. 출력하기
print(max(res_case))
print(min(res_case))
