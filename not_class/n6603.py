'''
6603번: 로또 / silver 2 / 조합
'''
import sys
import itertools

input = sys.stdin.readline

while True:
    lotto = list(map(int, input().split()))
    if lotto[0] == 0:
        break
    case = lotto[1:len(lotto)]
    case.sort()
    S = list(itertools.combinations(case, 6))
    for i in S:
        for j in i:
            print(j, end=' ')
        print()
    print()
