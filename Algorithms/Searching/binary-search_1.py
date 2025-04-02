# binary search - recursive approach

from typing import List

def binary_search(sorted_arr: List, key: int, a: int, b: int) -> int:
    if a == b:
        a = -1 if sorted_arr[a] != key else a
        return a
    elif a > b:
        return b

    c = (a+b)//2

    if key <= sorted_arr[c]:
        return binary_search(sorted_arr, key, a, c)
    else:
        return binary_search(sorted_arr, key, c+1, b)


array = []
key = 4
print(f"Index for {key} is {binary_search(array, key, 0, len(array)-1)}")


