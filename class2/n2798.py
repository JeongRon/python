"""
2798 - 블랙잭 (브론즈 2)
"""

N, M = map(int, input().split())

card = list(map(int, input().split()))

three_card_max = 0
for a in range(0, N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            three_card = card[a] + card[b] + card[c]
            if M >= three_card and three_card_max < three_card:
                three_card_max = three_card
print(three_card_max)


# review
# 1. 카드 입력을 card 인덱스에 넣는다
# 2. 각 인덱스 3개의 합을 구하기
# - 012 / 013 / 014 ... 3개의 카드 중복되지 않고 만나기 - for문 3개로 이용
# - 3개의 카드가 M을 넘지 않고 / 최대값인지
