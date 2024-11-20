import math 
from Factorization import factorization

def euler_totient(n):
    ret = 1

    factors = factorization(n)
    for key, value in factors.items():        
        ret *= (key - 1)*pow(key, value - 1)
    return ret

if __name__ == '__main__':

    n = 123456
    print("Euler Totient number of ", n, " is :", euler_totient(n))
    #for n in range(1, 11):
    #    print("Euler Totient number of ", n, " is :", euler_totient(n))