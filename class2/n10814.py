"""
10814 - 나이순 정렬 (silver 5)
"""
import sys

N = int(sys.stdin.readline())

online_list = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    online_list.append((age, name))

# sort 활용
online_list.sort(key=lambda x: x[0])

for i in online_list:
    print(i[0], i[1])

# review
# 내가 작성한 코드 - 시간초과 / sort함수 활용 방법 몰라서 버블정렬 사용
# import sys
# N = int(sys.stdin.readline())
# online_list = []
# for i in range(N):
#     member = list(sys.stdin.readline().split())
#     member[0] = int(member[0])
#     online_list.append(member)
# for i in range(N - 1, 0, -1):
#     for j in range(i):
#         if online_list[j][0] > online_list[j + 1][0]:
#             online_list[j], online_list[j + 1] = (
#                 online_list[j + 1],
#                 online_list[j],
#             )
# for i in range(N):
#     print(online_list[i][0], online_list[i][1])

# 참고 : https://velog.io/@1204jh/10814
