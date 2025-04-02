

def binary_search(sorted_list, key, a, b):
    if a > b:
        return b

    while a <= b:
        c = (a+b)//2

        if key == sorted_list[c]:
            return c
        elif key < sorted_list[c]:
            b = c-1
        else:
            a = c+1

    return -1

array = [1,2,4,5,5,5,6,7,10,13]
key = 7
print(f"Index for {key} is {binary_search(array, key, 0, len(array)-1)}")