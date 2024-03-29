"""
DP (다이나믹 프로그래밍) 사용 조건 
1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있음
2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결 함
메모이제이션 : 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념
"""
"""
피보나치 수열 : 탑다운 DP 방식
시간 복잡도 O(N)
"""
d = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


print(fibo(99))
