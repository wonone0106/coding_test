import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())

if n == 0:
    write('0')
    exit()

lst = [int(input()) for _ in range(n)]

cut = int(n * 0.15 + 0.5)

lst.sort()

lst = lst[cut:n-cut]

avg = int(sum(lst) / len(lst) + 0.5)

write(str(avg))