while True:
    triangle = list(map(int, input().split()))

    if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
        break

    triangle.sort()

    for i in range(3):
        triangle[i] *= triangle[i]

    if triangle[0] + triangle[1] == triangle[2]:
        print("right")
    else:
        print("wrong")
