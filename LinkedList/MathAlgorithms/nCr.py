import math 

def factorial_util(n, nemo):
    if n <= 1:        
        return 1
    
    if nemo[n] != -1:        
        return nemo[n]
    
    nemo[n] = n*factorial_util(n - 1, nemo)
    
    return nemo[n]

def nCr(n, r):
    nemo = [-1]*(n + 1)

    return factorial_util(n, nemo)/(factorial_util(r, nemo) * factorial_util(n - r, nemo))

if __name__ == '__main__':
    n = 5
    r = 2
    print("Combinations of ", r, " over ", n, " is: ", int(nCr(n, r)))