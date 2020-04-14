from random import randint
import random

arr_ = [randint(0, 1000) for i in range(25)]


def quick_sort(arr, fst, lst):
    if fst >= lst:
        return
    i, j = fst, lst
    target = arr[randint(fst, lst)]
    while i <= j:
        while arr[i] < target:
            i += 1
        while arr[j] > target:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    quick_sort(arr, fst, j)  # left
    quick_sort(arr, i, lst)  # right


def quick_sort_2(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
    left_nums = [n for n in arr if n < q]

    equip_nums = [q] * arr.count(q)
    right_nums = [n for n in arr if n > q]
    return quick_sort_2(left_nums) + equip_nums + quick_sort_2(right_nums)


print("Start array:\n", arr_)
print("Fast sort:\n", quick_sort_2(arr_))
quick_sort(arr_, 0, len(arr_) - 1)
print("Fastest sort:\n", arr_)
