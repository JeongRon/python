'''
5543번: 상근날드 / bronze 4 / 구현
'''
store = []
for _ in range(5):
    price = int(input())
    store.append(price)
burger = min(store[0], store[1], store[2])
drink = min(store[3], store[4])
print(burger + drink - 50)
