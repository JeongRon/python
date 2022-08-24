'''
1931 - 회의실 배정 (silver 1)
'''
import sys

input = sys.stdin.readline

meeting_lst = []
N = int(input().rstrip())

for _ in range(N):
    meeting_lst.append(tuple(map(int, input().split())))

# 1. 끝나는 시간 오름차순 (그리디)
# 2. 시작하는 시간 오름차순 ex => (2,2),(1,2)  
meeting_lst.sort(key=lambda x : (x[1], x[0]))

time = 0
count = 0
for meeting in meeting_lst:
    if time <= meeting[0]:
        count += 1
        time = meeting[1]
print(count)