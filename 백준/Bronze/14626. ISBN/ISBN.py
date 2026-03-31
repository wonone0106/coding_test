s = input()

temp = 0
x = 0

for i in range(len(s)):
    try:
        if i % 2 == 0:
            temp += int(s[i])
        else:
            temp += int(s[i]) * 3
    except:
        if i % 2 == 0:
            x = 1
        else:
            x = 3

for i in range(10):
    if (temp + i * x) % 10 == 0:
        print(i)
        break