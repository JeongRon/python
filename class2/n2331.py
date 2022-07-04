"""
2331 - 분해합  
"""
N = int(input())


for i in range(N):
    creator = [i]
    while True:
        if i // 10 == 0:
            creator.append(i % 10)
            break
        else:
            creator.append(i % 10)
            i = i // 10
    if sum(creator) == N:
        print(creator[0])
        break
    if creator[0] == N - 1:
        print(0)

# review
# - 생성자는 분해합 숫자보다 작아야 함
# - 따라서 0 ~ (분해합 -1) 차례로 생성자를 확인 하는 코드를 짬
#     - creator 인덱스는 분해합을 담을 리스트
#     - 198 -> creator[198, 8, 9, 1] list가 담기도록 설정
#     - sum(creator) 함수로 생성자를 확인
#     - (분해합 -1) 까지 모두 돌았는데 없으면 0출력
