import math 

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

# Given a number n, return all prime factors of n
def prime_factors(n):
    primes = sieve_eratosthenes(math.floor(math.sqrt(n)))
    prime_factors = []

    for k in primes:
        if n % k == 0:
            prime_factors += [k]
    
    return prime_factors

# Given a number n, factorize it 
def factorization(n):
    primes = sieve_eratosthenes(int(math.sqrt(n)))
    factors = {}

    for prime in primes:        
        if n % prime == 0:                 
            exp = 0
            while n % prime == 0:
                n /= prime                   
                exp += 1
            factors[prime] = exp  
    if n != 1:
        factors[int(n)] = 1
    return factors


if __name__ == '__main__':
    n = 15  
    print(f"Primes smaller than {n} is: {sieve_eratosthenes(n)}")    
    factors = factorization(n)
    print(f"Factorization of {n} is:", end = ' ')
    for key, value in factors.items(): 
        print(f"{key}^{value}", end=' ')
    print()
