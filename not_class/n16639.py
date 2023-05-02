'''
16639번: 괄호 추가하기 3 / gold 1 / DP
'''
import sys

input = sys.stdin.readline


# a와 b를 계산해서 리턴하는 함수
def calculator(a, op, b):
    if op == '-':
        return a - b
    elif op == '+':
        return a + b
    elif op == '*':
        return a * b


# dp[x][y] 자리의 최솟값 최대값 구해서 리턴하는 함수
def find_min_max(x, y, i, j):
    value_list = []
    while True:
        if j == y:
            break
        value_list.append(calculator(dp[x][j][0], op_list[j], dp[i][y][0]))
        value_list.append(calculator(dp[x][j][0], op_list[j], dp[i][y][1]))
        value_list.append(calculator(dp[x][j][1], op_list[j], dp[i][y][0]))
        value_list.append(calculator(dp[x][j][1], op_list[j], dp[i][y][1]))
        i += 1
        j += 1
    return min(value_list), max(value_list)


# 수식길이: n, 수식: expression 입력받기
n = int(input())
expression = input().rstrip()
# 연산자 리스트, 정수 리스트 따로 분류하기
op_list = []
num_list = []
for i in range(len(expression)):
    if i % 2 == 0:
        num_list.append(int(expression[i]))
    else:
        op_list.append(expression[i])
num_cnt = len(num_list)
# dp 리스트 만들기
dp = [[[0, 0] for _ in range(num_cnt)] for _ in range(num_cnt)]
# dp 리스트 채우기
for x in range(num_cnt - 1, -1, -1):
    j = x
    for y in range(x, num_cnt):
        if x == y:
            dp[x][y][0] = num_list[x]
            dp[x][y][1] = num_list[x]
        else:
            i = x + 1
            max_value, min_value = find_min_max(x, y, i, j)
            dp[x][y][0] = min_value
            dp[x][y][1] = max_value
# 출력하기
print(max(dp[0][-1]))
