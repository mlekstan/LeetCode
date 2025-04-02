# binary search - iterative approach

from typing import List

def binary_search(sorted_array: List, key: int, a: int , b: int ) -> int:
    if a > b:
        return b
    
    c = (a+b)//2
    
    while key != sorted_array[c]:
        if a == b == c:
            return -1

        if key < sorted_array[c]:
            b = c 
        else:
            a = c+1
        
        c = (a+b)//2
        
    return c


array = []
key = 4
print(f"Index for {key} is {binary_search(array, key, 0, len(array)-1)}")