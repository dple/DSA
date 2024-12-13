import math 

def binomial_coeff_util(n, k, nemo):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    
    if nemo[n][k] != -1:
        return nemo[n][k]
    
    nemo[n][k] = binomial_coeff_util(n - 1, k - 1, nemo) + binomial_coeff_util(n - 1, k, nemo)

    return nemo[n][k]

def binomial_coeff(n, k):
    nemo = [[-1] * n] *k

    return binomial_coeff_util(n, k, nemo)


if __name__ == '__main__':
    n = 5
    k = 2
    print("# of", k, "cobinations of ", n, "is: ", binomial_coeff(n, k))
    