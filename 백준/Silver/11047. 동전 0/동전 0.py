n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst = lst[: :-1]
cnt = 0
for i in lst:
    if k - i >= 0:
        cnt += k // i
        k %= i
        if k == 0:
            print(cnt)
            break