import sys
import time

def double_factorial_iter(n, p):
    if n < 3:   # n = 1, 2
        return n
    else:
        return (double_factorial_iter(n-2, p) * n) % p

def double_factorial(n):
    p = MERSENNE_PRIME

    # prime is factor of double factorial
    if (n >= p): 
        return 0

    # since recursion is limited => use loop instead
    # solve limited variable storage
    result = 1
    for i in range(1, n+1, 2):
        result = (result * i) % p  
  
    return result

# n must be odd
MERSENNE_PRIME = 2147483647
print(double_factorial(7))
print(double_factorial(31))
print(double_factorial(127))
print(double_factorial(8191))
print(double_factorial(131071))
print(double_factorial(524287))
start = time.time()
print(double_factorial(99999999)) # spend
end = time.time()
print('Spend: ', end - start)
print(double_factorial(MERSENNE_PRIME))