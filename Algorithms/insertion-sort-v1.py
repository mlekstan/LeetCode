# insertion-sort (version 1)

from time import perf_counter

def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(0, i):
            if A[j] > A[i]:
                B = A[j:i]
                A[j] = A[i]
                A[j+1:i+1] = B
    


table = [7,6,5,8,7,8,7,8,8,9,3,2,1,5,7,8,7,9,9,0]

start_time = perf_counter()
insertion_sort(table)
end_time = perf_counter()

ex_time = end_time - start_time
print(table, 'time = ', ex_time)