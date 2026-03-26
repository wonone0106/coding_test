import sys

input = sys.stdin.readline
n = int(input())

p = list(map(int, input().split()))

p.sort(reverse=True)

s = 0

for i in range(n):
    s += sum(p[i:n])
    
print(s)