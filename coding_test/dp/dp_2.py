"""
피보나치 수열 : 보텀업 DP 방식
- 작은 문제를 조합해서 큰 문제를 차례대로 해결하는 방식
"""
# DP 테이블 초기화
d = [0] * 100

# 첫 번째, 두 번째 피보나치 수 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 (보텀업 DP)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
