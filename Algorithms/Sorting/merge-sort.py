# merge-sort, pes: O(nlgn)

from time import perf_counter
from math import floor

def merge(A, p, q, r):
    
    L = A[p:q+1]
    P = A[q+1:r+1]
    L_len = (q+1)-p
    P_len = (r+1)-(q+1)

    i = 0
    j = 0
    k = p
    while i < L_len and j < P_len:
        if L[i] > P[j]:
            x = P[j]
            A[k] = x
            j += 1
        
        else:
            x = L[i]
            A[k] = x
            i += 1

        k += 1

    if i == L_len:
        A[k:r+1] = P[j:P_len]
    elif j == P_len:
        A[k:r+1] = L[i:L_len]



def merge_sort(A, p, r):
    if p < r:
        q = floor((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)



table = [7,6,5,8,7,8,7,8,8,9,3,2,1,5,7,8,7,9,9,0]

start_time = perf_counter()
merge_sort(table, 0, len(table)-1)
end_time = perf_counter()

ex_time = end_time - start_time
print(table, 'time = ', ex_time)