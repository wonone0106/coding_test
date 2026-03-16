import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())

lst = [int(input()) for _ in range(n)]

lst.sort()
for i in lst:
    write(str(i) + "\n")