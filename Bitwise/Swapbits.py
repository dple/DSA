from Bitwise import length

"""
Given an integer x, two position p1, p2, and a number n. Swap n bits of x starting from p1 to n bits starting from p2
Using string in Python
"""
def swapbits_string(x, p1, p2, n):
    
    s_x = format(x, 'b')    

    if p1 == p2:
        return x
    
    if p1 + n > p2: 
        print("There is an overlap in replacing")
        return 
    
    if (len(s_x) < p2 + n):
        s_x = '0' * (p2 + n - len(s_x)) + s_x

    print("Original number in binary format: ", s_x)

    l = len(s_x)
    
    s_x = s_x[:l - n - p2] + s_x[l - p1 - n: l - p1] + s_x[l - p2:l - p1 - n] + s_x[l - p2 - n: l - p2] + s_x[l - p1:]

    print("Replaced number in binary format is: ", s_x)

    return int(s_x, 2)
    

"""
Using the fact: 
    x ^ x = 0
    x ^ 0 = x, 
Hence, 
    sub1 ^ sub2 ^ sub1 = sub2
    sub1 ^ sub2 ^ sub2 = sub1
"""
def swapbits(x, p1, p2, n) :
     
    # xor contains xor of two sets 
    xor = (((x >> p1) ^ (x >> p2)) & ((1 << n) - 1))
  
    # To swap two sets, we need to again XOR the xor with original sets 
    return x ^ ( (xor << p1) | (xor << p2))

def swapbits1(x, p1, p2, n):
    print("Orgiginal number: ", format(x, 'b'))
    sub1 = (x >> p1) & ((1 << n) - 1)       # Get n bits starting from position p1
    sub2 = (x >> p2) & ((1 << n) - 1)       # Get n bits starting from position p2

    xor = sub1 ^ sub2                       # 

    mask = (xor << p2) | (xor << p1)

    print("Maks = ", format(mask, 'b'))

    print("Replaced number in binary", format(x ^ mask, 'b'))
    return x ^ mask 

# Using bitwise operations. Get trunks of bits, then use left shift operation to get back the number 
def swapbits2(x, p1, p2, n):
    if p1 + n > p2: 
        print("There is an overlap in replacing")
        return
    print("Original number in binary format: ", format(x, 'b'))
    
    sub1 = (x >> p1) & ((1 << n) - 1)
    print("Lower sub: ", format(sub1, 'b'))
    sub2 = (x >> p2) & ((1 << n) - 1)
    print("Upper sub:", format(sub2, 'b'))
    upper = x >> (p2 + n)
    print("MSBs: ", format(upper, 'b'))
    lower = x & ((1 << p1) - 1)
    print("LSBs: ", format(lower, 'b'))
    middle = (x >> (p1 + n) ) & ((1 << (p2 - p1 - n)) - 1)
    print("Middle bits: ", format(middle, 'b'))

    x = ((((((((upper << n)) + sub1) << (p2 - p1 - n)) + middle) << n) + sub2) << p1) + lower
    print("Replaced number in binary format is: ", format(x, 'b'))
    return x


if __name__ == '__main__':
    x, p1, p2, n = 47, 1, 5, 3    #    x, p1, p2, n = 28, 0, 3, 2

    print("Replaced number: ", swapbits(x, p1, p2, n))
    