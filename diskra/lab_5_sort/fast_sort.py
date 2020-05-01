from random import randint
import random


arr_ = [randint(0, 1000) for i in range(25)]


# Faster
def quick_sort(arr, fst, lst):
    if fst >= lst: return
    i, j = fst, lst
    target = arr[randint(fst, lst)]
    while i <= j:
        while arr[i] < target: i += 1
        while arr[j] > target: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    quick_sort(arr, fst, j)  # left
    quick_sort(arr, i, lst)  # right


# Slower, but less lines in func
def quick_sort_2(arr):
    if len(arr) <= 1: return arr
    q = random.choice(arr)
    left_nums, equip_nums, right_nums = [n for n in arr if n < q],[q] * arr.count(q),[n for n in arr if n > q]
    return quick_sort_2(left_nums) + equip_nums + quick_sort_2(right_nums)


if __name__ == "__main__":
    print("Start array:\n", arr_)
    print("Fast sort:\n", quick_sort_2(arr_))
    quick_sort(arr_, 0, len(arr_) - 1)
    print("Fastest sort:\n", arr_)
