"""
개미 전사 문제
점화식 / a(i) = max(a(i-1), a(i-2) + k(i))
"""
n = int(input())
array = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

# i-1 까지 터는 있는 경우 / i-2 까지 터는 경우 + i 번째 터는 경우
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
