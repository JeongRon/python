"""
모험가 길드
1.오름차순으로 정렬
2. 0번 인덱스 부터 하나씩 확인 
-> '현재 그룹에 포함된 모험가의 수'가
-> '현재 확인하고 있는 공포도' 보다 크거나 같으면 
-> 그룹 설정
"""
n = int(input())
data = list(map(int, input().split()))
data.sort()

group = 0
wait = 0

for i in data:
    wait += 1
    if i <= wait:
        group += 1
        wait = 0

print(group)
