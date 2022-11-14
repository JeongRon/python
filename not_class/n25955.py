"""
25955 - APC는 쉬운 난이도 순일까, 아닐까? / silver 4 / sorted, lambda
"""

n = int(input())
input_list = input().split()

tier_list = []
tier_dict = {"B": 0, "S": 1, "G": 2, "P": 3, "D": 4}
for i in range(n):
    now_tier = tier_dict[input_list[i][0]]
    now_num = int(input_list[i][1:])
    tier_list.append((now_tier, now_num))
temp_list = sorted(tier_list, key=lambda x: (x[0], -x[1]))

wrong_index = []
for i in range(n):
    if tier_list[i] != temp_list[i]:
        wrong_index.append(i)

if wrong_index:
    print("KO")
    print(input_list[wrong_index[1]], input_list[wrong_index[0]])
else:
    print("OK")
