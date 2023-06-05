'''
2309번: 일곱 난쟁이 / bronze 1 / 구현
'''
import itertools

dwarf = []
for _ in range(9):
    cm = int(input())
    dwarf.append(cm)
find = itertools.combinations(dwarf, 7)
for case in find:
    if sum(case) == 100:
        catch = list(case)
        break
catch.sort()
for i in catch:
    print(i)
