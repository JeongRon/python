"""
1로 만들기
1. X가 5로 나누어 떨어지면, 5로 나눈다
2. X가 3으로 나누어 떨어지면, 3으로 나눈다
3. X가 2로 나누어 떨어지면, 2로 나눈다
4. X에서 1을 뺀다

점화식 / a(i) = min(a(i-1), a(i/2), a(i/3), a(i/5)) + 1
"""

x = int(input())

# DP 테이블 초기화
d = [0] * 30001

# DP 보텀업
for i in range(2, x + 1):
    # 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
