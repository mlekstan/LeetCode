# sum of the elements of sequence

from time import perf_counter

def sum_recur(A, n):
    if n >= 1:
        n -= 1
        sum = sum_recur(A, n)
        sum += A[n]
    else:
        sum = 0
    
    return sum

def sum_iter(A, n):
    sum = 0
    for i in range(n):
        sum += A[i]
    
    return sum



table = [7,6,5,8,7,8,7,8,8,9,3,2,1,5,7,8,7,9,9,7,5,6,4,6,4,3,5,3,4,5,3,2,5,2,5,2,5,6,3,6,5,7,6,6,7,8,7,6,8,7,6,7,5,6,7,4,1,4,1,4,3,6,5,4,7,5,7,8,8,7,9,8,9,8,0]
n = len(table)

if True:
    start_time = perf_counter()
    sum = sum_recur(table, n)
    end_time = perf_counter()
else:
    start_time = perf_counter()
    sum = sum_iter(table, n)
    end_time = perf_counter()

print('sum =', sum, ';time =', end_time-start_time)