'''
2845번: 파티가 끝나고 난 뒤 / bronze 4 / 구현
'''
L, P = map(int, input().split())
people = list(map(int, input().split()))
cnt = L * P
for p in people:
    print(p - cnt, end=' ')
