import sys

input = sys.stdin.readline

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)

t = int(input())


for _ in range(t):
    k = int(input()) + 1
    n = int(input()) + k - 1
    
    result = factorial(n) // (factorial(k) * factorial(n - k))
    print(result)