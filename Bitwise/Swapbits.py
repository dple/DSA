from Bitwise import 
"""
Given an integer x, two position p1, p2, and a number n. Swap n bits of x starting from p1 to n bits starting from p2
"""
def swapbits(x, p1, p2, n):
    mask = 0
    for _ in range(n):


if __name__ == '__main__':
    x, p1, p2, n = 47, 1, 5, 3
    print("Binary of x:", format(x, 'b'))
    print("Binary of swapped x:", format(swapbits(x, p1, p2, n), 'b'))
    