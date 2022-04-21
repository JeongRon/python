"""
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""
# 1. num 입력
# 2. for 문
num = int(input())

for i in range(1, (num + 1)):
    print("*" * i)

# 피드백
# - for 구문
#   - range() 함수 이해
#       - 첫째 인자로 초기값, 둘째 인자로 종료값, (마지막 인자로 증가값)
#   - 문자열 곱하기 가능
