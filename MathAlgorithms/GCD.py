from functools import reduce
import math 

# Find the greatest common divisor of two given integers by using Euclidean method 
def Euclidean_recursive_gcd_by_subtraction(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    
    if a == b:
        return a
    
    if a > b:
        if a % b == 0:
            return b
        return Euclidean_recursive_gcd_by_subtraction(a - b, b)
    else:
        if b % a == 0:
            return a
        return Euclidean_recursive_gcd_by_subtraction(a, b - a)
    

def Euclidean_recursive_gcd_by_division(a, b):
    if b == 0:
        return a
    
    return Euclidean_recursive_gcd_by_division(b, a%b)

def Euclidean_iterative_gcd_by_division(a, b):
    
    while a > 0 and b > 0:
        
        if a > b: 
            a = a % b

        else:
            b = b % a

    if a == 0:
        return b
    return a

def gcd(a, b):
    return Euclidean_iterative_gcd_by_division(a, b)


# Find the GCD of an aray
def gcd_array(A):
    l = len(A)

    if l < 2:
        return 0 
    
    c = gcd(A[0], A[1])

    for i in range(2, l):
        c = gcd(c, A[i])

    return c

def gcd_array_reduce(A):
    return reduce(lambda x, y: gcd(x, y), A)

# Find LCM by using GCD: LCM(a, b) = a*b/gcd(a, b)
def lcm_gcd(a, b):
    return (a // gcd(a, b))*b

# Find LCM of two given numbers. 
def lcm_without_gcd(a, b):
    if a > b:
        small = b
        big = a
    else:
        small = a 
        big = b 
    # LCM will be the smallest multiple of the bigger number that is divisible by the smaller number 
    for i in range(big, a*b + 1, big):
        if i % small == 0:
            return i 

def lcm(a, b):
    return lcm_without_gcd(a, b)

def lcm_array(A):
    if len(A) < 2:
        return A[0]
    
    lm = lcm(A[0], A[1])

    for i in range(2, len(A)):
        lm = lcm(lm, A[i])
    
    return lm 

def lcm_array_reduce(A):
    return reduce(lambda x, y: lcm(x, y), A)

def isCoprime(a, b):
    if gcd(a, b) > 1:
        return False
    return True 

# Given a number n, return all prime numbers that are smaller or equal to n
def sieve_eratosthenes(n):
    primes = [i for i in range(2, n + 1)]    
    k = 2
    pos = 0
    while pos <= len(primes):
        pos += 1
        for i in range(k, n // k + 1):            
            if k*i in primes:
                primes.remove(k * i)    # Delete all multiple of k in the list         
        if pos < len(primes):
            k = primes[pos]        
    return primes 


# Find LCM of all first n natural numbers 
def lcmN(n):
    prime_factors = sieve_eratosthenes(n)
    lcm = 1
    
    for prime in prime_factors:
        power = int(math.log(n, prime))
        lcm *= prime ** power
    
    return lcm 


# Given gcd(a, b) and lcm(a, b), find possible pair a, b
def find_ab(g, l):
    if l % g != 0:
        return 0
    
    prod = l * g
    #list = []
    count = 0
    for a in range(g, int(math.sqrt(prod) + 1), g):
        b = prod / a 
        if b % g == 0:
            #list += [(a, int(b))]
            #list += [(int(b), a)]
            count += 2

    return count #list 

if __name__ == '__main__':
    #print("Enter two positive integers:")

    #a = int(input().strip())
    #b = int(input().strip())

    #print("GCD of (a, b) is: ", gcd(a, b))  
    n = 700  
    #print(f"Primes smaller than {n} is: {sieve_eratosthenes(n)}")
    #print(f"LCM of first {n} natural numbers is: {lcmN(n)}")    
    A = [12, 9, 15, 24, 27, 2]
    
    print("Number of possible of (a, b) is: ", find_ab(2, 12))

    #A = [ 4, 6, 8 ]
    #print("GCD of an array A is: ", gcd_array_reduce(A))
    #print("LCM of an array A is: ", lcm_array_reduce(A))
