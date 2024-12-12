"""
Convert Binary to GrayCode using Bitwise operations 
"""

def bin2gray(n):    
    return n ^ (n >> 1)

def gray2bin(n):
    gray = n

    while n > 0:
        n >>= 1
        gray ^= n
        
    return gray 

if __name__ == '__main__':
    n = 9    
    print("Binary string of ", n, "is: ", format(n, 'b'))
    gray = bin2gray(n)
    print("Gray code of ", n, "is: ", format(gray, 'b'))        
    print("Revert to binary:", format(gray2bin(gray), 'b'))