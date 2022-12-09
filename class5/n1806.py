"""
1806번 - 부분합 / gold 4 / 투 포인터
"""
import sys

input = sys.stdin.readline
INF = int(1e9)

n, s = map(int, input().split())
seq = list(map(int, input().split()))
# 리스트 앞에 0을 추가 / start 포인터가 처음에 가리키는 값
seq = [0] + seq
# 누적 합으로 바꾸기
for i in range(1, n + 1):
    seq[i] = seq[i - 1] + seq[i]

# seq 누적 합 리스트의 마지막 인덱스는 모든 값들을 합한 것
# 만일 모든 값들을 합한 것보다 s가 크면 바로 0 출력
if seq[-1] < s:
    print(0)
else:
    # 투 포인터 알고리즘 시작
    start = 0
    end = 1
    min_len = INF

    while start != n:
        if seq[end] - seq[start] >= s:
            if end - start < min_len:
                min_len = end - start
            start += 1
        else:
            if end != n:
                end += 1
            else:
                start += 1
    print(min_len)
