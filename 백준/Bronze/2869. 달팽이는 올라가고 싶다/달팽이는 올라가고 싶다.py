a, b, v = map(int, input().split())
v -= a
day = 0
if v == 0:
    print(1)
elif v > 0:
    day = v // (a - b)
    if v % (a - b) != 0:
        day += 1
    print(day + 1)
