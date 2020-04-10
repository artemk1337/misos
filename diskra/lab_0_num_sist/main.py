k = int(input("Выберете систему счисления: "))
n = eval(input("Введите выражение: "))

arr = []
while n > 0:
    n, a = divmod(n, k)
    arr = [a] + arr

arr = [x if (x < 10) else (chr(ord('A') + x - 10)) for x in arr]
for x in arr:
    print(x, end='')
