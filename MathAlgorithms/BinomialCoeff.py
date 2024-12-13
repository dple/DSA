def binomial_coeff_util(n, k, nemo):    
    if k > n:        
        return 0
    if k == 0 or k == n:
        nemo[n][k] = 1
        return 1
    
    if (k == 1) or (k == (n - 1)):
        nemo[n][k] = n        
        return n

    if nemo[n][k] != 0:    
        return nemo[n][k]
        
    nemo[n][k] = binomial_coeff_util(n - 1, k - 1, nemo) + binomial_coeff_util(n - 1, k, nemo)
    
    return nemo[n][k]

def binomial_coeff(n, k):
    nemo = [[0 for _ in range(k + 1)] for _ in range(n + 1)] #[[0] * (k + 1)] * (n + 1)    
    return binomial_coeff_util(n, k, nemo)


if __name__ == '__main__':
    n = 8
    k = 4
    print("Number of", k, "combinations of ", n, "is: ", binomial_coeff(n, k))
    