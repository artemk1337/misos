
sist = 7


s = "65 + 422".split(' ')
n1 = [int(x) for x in list(s[0])]
n2 = [int(x) for x in list(s[-1])]

n1.reverse()
n2.reverse()


def summa():
    def sum_(n1, n2):
        while len(n1) >= len(n2):
            n2 += [0]
        return [i + j for i, j in zip(n1, n2)]

    if len(n1) >= len(n2):
        arr = sum_(n1, n2)
    else:
        arr = sum_(n2, n1)

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
    [print(x, end='') for x in arr]


summa()



