n = int(input())
L = [list(input().split()) for i in range(n)]

L.sort(key=lambda x: int(x[0]))

for i in range(n):
    print(' '.join(L[i]))