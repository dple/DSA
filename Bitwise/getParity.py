def get_parity(n):
    parity = 0
    while (n != 0):
        parity ^= 1
        n &= (n - 1)
    
    return parity

if __name__ == '__main__':
    n = 47
    print(format(n, 'b'))
    print(get_parity(n))