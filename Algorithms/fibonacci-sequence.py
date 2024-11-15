# Fibonacci sequence

from time import perf_counter

def fibonacci_recur_1(n):
    if n > 2:
        n -= 1
        seq = fibonacci_recur_1(n)
        seq.append(seq[-1] + seq[-2])
    
    else:
        seq = [0, 1]
        seq = seq[0:n]

    return seq

def fibonacci_recur_2(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = fibonacci_recur_2(n - 1)
    sequence.append(sequence[-1] + sequence[-2])
    
    return sequence


def fibonacci_iter(n):
    seq = [0, 1]
    if n < 3:
        seq = seq[0:n]
    else:
        for i in range(n-2):
            seq.append(seq[i]+seq[i+1])
    
    return seq


n = 35

if True:
    start_time = perf_counter()
    sequence = fibonacci_recur_1(n)
    end_time = perf_counter()
elif False:
    start_time = perf_counter()
    sequence = fibonacci_recur_2(n)
    end_time = perf_counter()
else:
    start_time = perf_counter()
    sequence = fibonacci_iter(n)
    end_time = perf_counter()
print('sequence =', sequence, ';time =', end_time-start_time)