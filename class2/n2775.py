"""
2775 - 부녀회장이 될테야 (bronze 1)
"""

T = int(input())


for _ in range(T):
    building = int(input())
    unit = int(input())
    # 0층 원하는 호수 만큼 인덱스 추가
    Apartment = [i for i in range(1, unit + 1)]
    for y in range(1, building + 1):
        for x in range(1, unit):
            Apartment[x] = Apartment[x - 1] + Apartment[x]
    print(Apartment[-1])

# review
# 재귀함수 이용해서 거주민 수 출력 -> 시간초과
# 1. 입력 호수 만큼 인덱스 크기 지정해서 0층의 값들을 넣음
# 2. 입력된 층 만큼 차례로 1,2,3,...층 까지 해당 인덱스가 변경
# 원하는 값이 마지막 인덱스 -> 출력
