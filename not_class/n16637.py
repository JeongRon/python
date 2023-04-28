'''
16637번: 괄호 추가하기 / gold 3 / 브루트포스
'''
import sys
import itertools

input = sys.stdin.readline


# a와 b를 연산해주고 결과를 리턴하는 함수
def calculator(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b


# 괄호가 있는 연산자 인덱스 case 포함, 식 계산하는 함수
def case_result(case):
    i = 0
    if 0 in case:
        res = calculator(num_lst[0], op_lst[0], num_lst[1])
        i += 1
    else:
        res = num_lst[0]
    while i <= len(op_lst) - 1:
        if i + 1 in case:
            tmp = calculator(num_lst[i + 1], op_lst[i + 1], num_lst[i + 2])
            res = calculator(res, op_lst[i], tmp)
            i += 2
        else:
            res = calculator(res, op_lst[i], num_lst[i + 1])
            i += 1
    return res


# 괄호 (1~max_bracket)개 일때의 경우를 만드는 함수
def make_case():
    case = [()]
    op_case = [i for i in range(len(op_lst))]
    max_bracket = len(num_lst) // 2
    bracket = 1
    while bracket <= max_bracket:
        tmp_case = itertools.combinations(op_case, bracket)
        case += tmp_case
        bracket += 1
    return case


# 괄호 케이스 적합한지 체크하는 함수
def check_case(case):
    flag = True
    if len(case) >= 2:
        for i in range(1, len(case) - 1):
            if case[i - 1] == case[i] - 1:
                flag = False
    return flag


def max_result():
    # 괄호 케이스들 만들기
    parentheses_case = make_case()
    max_res = -int(1e9)
    # 괄호 케이스 하나씩 확인하기
    for case in parentheses_case:
        # 만일, 해당 괄호 케이스가 적합하다면, 괄호 케이스를 적용해서 식 결과 계산
        if check_case(case):
            res = case_result(case)
            if max_res < res:
                max_res = res
    print(max_res)


# 수식의 길이 N, 수식 expression 입력받기
N = int(input())
expression = input().rstrip()
# 입력받은 수식을 숫자, 연산자 분류하기
num_lst = []
op_lst = []
for i in range(len(expression)):
    if i % 2 == 0:
        num_lst.append(int(expression[i]))
    else:
        op_lst.append(expression[i])
# 결과값 구하기
max_result()
