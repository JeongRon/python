'''
1072번: 게임 / silver 3 / 이분탐색
'''

game, win = map(int, input().split())
rate = (win * 100) // game
if rate >= 99:
    print(-1)
else:
    res = 0
    start = 1
    end = game
    while start <= end:
        mid = (start + end) // 2
        new_odds = (win + mid) * 100 // (game + mid)
        if new_odds <= rate:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    print(res)
