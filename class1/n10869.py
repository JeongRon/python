"""
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오
입력 :
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
출력 :
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다
"""
# 1. A와 B input()
# 2. A와 B string타입에서 int타입으로 바꾸기
# 3. print하기

A, B = input().split()
A = int(A)
B = int(B)
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)

# point
# - A와 B 한줄에 값을 입력 받는 방법
# - input()으로 값을 입력 받으면 string 타입이므로 타입 변환 필요
# - A/B는 파이썬에서 실수로 출력되므로 원하는 결과를 얻기 위해서는 int로 형 변환 시켜줘야 한다.
# - 정수 나누기도 사용 가능 A//B
