"""
효율적인 화폐 구성
"""
# n, m 입력 받기 (n:화폐종류 개수 , m: 최종 m원)
n, m = map(int, input().split())
# n개의 화폐 단위 정보를 입력 받기
array = []
for _ in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)
d[0] = 0

# DP 보텀업
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 출력
if d[m] == 10001: # M원을 만드는 방법 없는 경우
    print(-1)
else:
    print(d[m])