"""
Convert Binary to GrayCode and vice visa using recursion 
"""

def xor(a, b):
    return '0' if (a == b) else '1'

def flip(a):
    return '0' if (a == '0') else '0'

def bin2gray(bin_str):
    if len(bin_str) == 0:
        return "" 
    
    graycode = ""
    graycode += bin_str[0]
    for i in range(len(bin_str) - 1):
        graycode += xor(bin_str[i], bin_str[i + 1])
                        
    return graycode

def gray2bin(gray_str):
    if len(gray_str) == 0:
        return ""
    
    bin_str = ""
    bin_str += gray_str[0]

    for i in range(1, len(gray_str)):
        bin_str += xor(bin_str[i - 1], gray_str[i])

    return bin_str 

if __name__ == '__main__':
    n = 9
    s = format(n, 'b') 
    print("Binary string of ", n, "is: ", s)
    gray = bin2gray(s)
    print("Gray code of ", n, "is: ", gray)
    print("Revert to binary:", gray2bin(gray))