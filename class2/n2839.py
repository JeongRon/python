"""
2839 - 설탕 배달 (silver 4)
"""
import sys

input = sys.stdin.readline

N = int(input())

count = 0
if N % 5 == 0:
    count = N // 5
else:
    while N > 0:
        N -= 3
        count += 1
        if N % 5 == 0:
            count += N // 5
            break
        elif N == 1 or N == 2:
            count = -1
            break
        elif N == 0:
            break
print(count)

# review
# 참고 https://puleugo.tistory.com/27
# 반복문을 통해서 문제 해결 가능
# 5의배수, 3의배수, 5와 3이 쓰일 때 , 그 외 등의 조건문으로 문제 풀이
# 부족했던 부분 - 5와3 을 모두 쓸 때, N에서 3을 빼면서 비교하는 코드를 생각 못함
