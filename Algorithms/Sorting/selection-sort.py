# sorting using selection, O(n^2)

from time import perf_counter

def selection_sort(A):
    length = len(A)
    i = 0
    
    for j in range(0, length):    
        
        min = A[j]
        i_min = j
        for i in range(j+1, length):
            if (A[i] < min):
                min = A[i]
                i_min = i
        A[i_min] = A[j]
        A[j] = min

        

table = [7,6,5,8,7,8,7,8,8,9,3,2,1,5,7,8,7,9,9,0]

start_time = perf_counter()
selection_sort(table)
end_time = perf_counter()

ex_time = end_time - start_time
print(table, 'time = ', ex_time)

        
