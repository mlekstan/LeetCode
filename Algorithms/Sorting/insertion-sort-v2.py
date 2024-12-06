# insertion-sort (version 2), pes: O(n^2)

from time import perf_counter

def insertion_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        x = A[i]
        while (j >= 0 and A[j] > x):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = x

table = [7,6,5,8,7,8,7,8,8,9,3,2,1,5,7,8,7,9,9,0]

start_time = perf_counter()
insertion_sort(table)
end_time = perf_counter()

ex_time = end_time - start_time
print(table, 'time = ', ex_time)
