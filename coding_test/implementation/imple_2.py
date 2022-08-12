"""
시각 / 완전 탐색(Brute Forcing)

정수 N이 입력되면 00시 00분 00초 ~ N시 59분 59초까지
모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수
"""
N = int(input())
count = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1

print(count)
