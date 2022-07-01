x, y, w, h = map(int, input().split())

distance = [w - x, h - y, x, y]

minimum = min(distance)

print(minimum)

# 1. w - x
# 2. h - y
# 3. x
# 4. y
