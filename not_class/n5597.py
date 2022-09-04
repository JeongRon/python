"""
5597 - 과제 안 내신 분..? (bronze 5)
"""

student_list = {i for i in range(1, 31)}
for _ in range(28):
    n = int(input())
    student_list.remove(n)
print(min(student_list))
print(max(student_list))
