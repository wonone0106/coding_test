import sys

input = sys.stdin.readline
n = int(input())

count = -1
count_5 = n // 5
count_3 = n // 3

for i in range(count_5, -1, -1):
    for j in range(count_3, -1, -1):
        if 5 * i + 3 * j == n:
            count = i + j
            break
        else:
            count = -1
    if count != -1:
        break
print(count)