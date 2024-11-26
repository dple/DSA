import math 
from Factorization import factorization

def euler_totient(n):
    ret = 1

    factors = factorization(n)
    for prime, exponent in factors.items():        
        ret *= (prime - 1)*pow(prime, exponent - 1)
    return ret

if __name__ == '__main__':

    n = 123456
    print("Euler Totient number of ", n, " is :", euler_totient(n))
    