
sist = int(input('Введите сист. счисления: '))
s = str(input('Введите выражение: '))
s = s.split(' ')

n1 = [int(x) for x in list(s[0])]
n2 = [int(x) for x in list(s[-1])]

n1.reverse()
n2.reverse()


def summa():
    def add_0(n1, n2):
        while len(n1) >= len(n2):
            n2 += [0]
        return [i + j for i, j in zip(n1, n2)]

    def check_len():
        if len(n1) >= len(n2):
            arr = add_0(n1, n2)
        else:
            arr = add_0(n2, n1)
        return arr

    arr = check_len()
    idx = 0
    a = 0
    while True:
        if idx >= len(arr) and a == 0:
            break
        elif idx >= len(arr):
            arr += [0]
        arr[idx] += a
        a, lost = divmod(arr[idx], sist)
        arr[idx] = lost
        idx += 1

    arr.reverse()
    [print(x, end='') if x < 10 else print(chr(ord('a') + x - 10)) for x in arr]


def diff():
    def add_0(n1, n2):
        while len(n1) >= len(n2):
            n2 += [0]
        return [i - j for i, j in zip(n1, n2)]

    def check_len():
        if len(n1) >= len(n2):
            arr = add_0(n1, n2)
        else:
            arr = add_0(n2, n1)
        return arr

    arr = check_len()
    i = 0
    minus = 0
    print(arr)
    if arr[-1] < 0:
        arr = [i * (-1) for i in arr]
        minus = 1
    while i < len(arr):
        if arr[i] < 0:
            if i + 1 < len(arr):
                arr[i] += sist
                arr[i + 1] -= 1
        i += 1
    print(arr)
    arr.reverse()
    if minus == 1:
         print('-', end='')
    print(arr)
    [print(x, end='') if x < 10 else print(chr(ord('a') + x - 10)) for x in arr]


if s[1] == '+':
    summa()
elif s[1] == '-':
    diff()

