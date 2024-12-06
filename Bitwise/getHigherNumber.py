# Given a nunmber n, this code is for getting a next higher number having the same Hamming weight (number of bits 1) as n

def get_higher_number(n):
    pos, k = 0, 0
    if n == 0:
        return n
    if not (n & (n - 1)):
        return n << 1

    temp = n
    # Get the first bit '1' position from right of n
    # Pos will be the position of the most right bit 1
    while (temp > 0):
        if (temp & 1 == 0):
            pos += 1
            temp >>= 1
        else: 
            while (temp & 1):   # Get the right most string of 1's in n
                                # k will be the # of bits 1
                k += 1
                temp >>= 1
            temp = 0
    # Get (k + pos) bits of n from right
    sub = n & ((1 << (k + pos)) - 1)
    # Get the mask replacing sub in n
    mask = (1 << (k + pos)) + ((n >> (pos + 1)) & ((1 << k) - 1))
    xor = mask ^ sub
    # Replace sub string in n by using XOR: n ^ mask ^ sub (due to sub ^ sub = 0)
    return n ^ xor

if __name__ == '__main__':
    n = 156
    print("Binary of n is: ", bin(n))
    print("Binary of next higher number is: ", bin(get_higher_number(n)))