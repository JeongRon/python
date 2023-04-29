'''
7785번: 회사에 있는 사람 / silver 5 / 구현
'''
n = int(input())
company = set()
for _ in range(n):
    name, state = map(str, input().split())
    if state == 'enter':
        company.add(name)
    elif state == 'leave':
        company.remove(name)
company = list(company)
company.sort(reverse=True)
for i in company:
    print(i)
