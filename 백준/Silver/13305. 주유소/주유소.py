n = int(input())
N = list(map(int, input().split()))
price = list(map(int, input().split()))

total_price = 0
low_price = price[0]
total_length = N[0]

for i in range(n):
    if price[i] < low_price:
        low_price = price[i]
    try:
        total_length += N[i]
        total_price += low_price * N[i]
    except IndexError:
        pass

print(total_price)