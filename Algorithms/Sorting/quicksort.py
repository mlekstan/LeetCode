# qicksort, avg: O(nlgn), pes: O(n^2)

from time import perf_counter

def partition(A, p, r):
    i = p 
    j = r
    x = A[p]
    while True:   
        while A[j] > x:
            j -= 1
        while A[i] < x:
            i += 1
        if i < j:
            Ai = A[i]
            Aj = A[j]

            A[i] = Aj
            A[j] = Ai

            j -= 1
            i += 1
        else:
            return j

def quicksort(A, p, r):

    if (p < r):    
        q = partition(A, p ,r)
        quicksort(A, p, q)
        quicksort(A, q+1, r) 


table = [7,6,5,8,7,8,7,8,8,9,3,2,1,5,7,8,7,9,9,0]

start_time = perf_counter()
quicksort(table, 0, len(table)-1)
end_time = perf_counter()

ex_time = end_time - start_time
print(table, 'time = ', ex_time)