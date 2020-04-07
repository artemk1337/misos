import numpy as np

max_ = int(input("Выберет систему счисления: "))
s = input("Введите уравнение в формате 123 + 123: ")

arr1 = []
arr2 = []

oper = ''
s = list(s)
i = 0
while s[i] != ' ':
    if ord(s[i]) >= 97:
        s[i] = ord(s[i]) - ord('a') + 10
    arr1.append(int(s[i]))
    i += 1
i += 1
oper = s[i]
i += 2
while i < len(s):
    if ord(s[i]) >= 97:
        s[i] = ord(s[i]) - ord('a') + 10
    arr2.append(int(s[i]))
    i += 1


arr1, arr2 = arr1[::-1], arr2[::-1]
while len(arr1) < len(arr2):
    arr1.append(0)
while len(arr2) < len(arr1):
    arr2.append(0)


res = []
if oper == '+':
    res = np.sum([arr1, arr2], axis=0).tolist()
    i = 0
    while i < len(res) - 1:
        while res[i] >= max_:
            res[i] -= max_
            res[i + 1] += 1
        i += 1
    while True:
        if res[i] >= max_:
            res.append(0)
        else:
            break
        while res[i] >= max_:
            res[i] -= max_
            res[i + 1] += 1
        i += 1
elif oper == '-':
    res = np.sum([arr1, [-i for i in arr2]], axis=0)
    i = 0
    while i < len(res) - 1:
        while res[i] < 0:
            res[i + 1] -= 1
            res[i] += max_
        i += 1


for i in res[::-1]:
    if i >= 10:
        i -= 10
        print(chr(ord('a') + i), end='')
    else:
        print(i, end='')
