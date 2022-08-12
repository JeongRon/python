"""
1이 될 때까지 / 로그시간 복잡도
"""
# 1. n을 k로 나누어 떨어지는 수를 찾기 위해 -1을 계속 실행
# 2. (1)번의 수와 k를 계속 나누기

n, k = map(int, input().split())

result = 0

while True:
    # target : n에서 가장 근접한 k로 나누어 떨어지는 수 찾기
    target = (n // k) * k
    # result : n이 k로 나누어 떨어지는 수가 될 때까지 뺀 횟수
    result += n - target
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += n - 1
print(result)
