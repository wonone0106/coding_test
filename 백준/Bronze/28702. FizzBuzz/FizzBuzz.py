import sys

input = sys.stdin.readline
write = sys.stdout.write

lst = []
for _ in range(3):
    lst.append(input())

cnt = 3   


for i in range(3):
    try:
        num = int(lst[i])
        break
    except:
        pass
    cnt -= 1

a = num + cnt

if a % 15 == 0:
    write('FizzBuzz')
elif a % 5 == 0:
    write('Buzz')
elif a % 3 == 0:
    write('Fizz')
else:
    write(str(a))