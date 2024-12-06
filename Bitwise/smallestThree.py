import sys 

# Find min & max without branching 

BYTE = 8
INT_BYTES = sys.getsizeof(int())
INT_BITS = BYTE * INT_BYTES

def min1(x, y):
    return y ^ ((x ^ y) & -(x < y))

def min2(x, y):
    return y + ((x - y) & ((x - y) >> INT_BITS))
                
def max1(x, y):
    return x ^ ((x ^ y) & -(x < y))

def max2(x, y):
    return x - ((x - y) & ((x - y) >> INT_BITS))

def min_of_three(x, y, z):
    t = min2(x, y)
    return min2(t, z)

def max_of_three(x, y, z):
    t = max2(x, y)
    return max2(t, z)

if __name__ == '__main__':
    x, y, z = 15, 13, 17
    print("Mim value of x and y: ", min2(x, y))
    print("Min of three numbers: ", min_of_three(x, y, z))
    print("Max of three numbers: ", max_of_three(x, y, z))
    