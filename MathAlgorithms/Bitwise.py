# Get a bit of n at a specific index 
def get_bit(value, bit_index):
    return (value & (1 << bit_index)) >> bit_index
    

if __name__ == '__main__':
    a = 5   # a = 0000 0101
    b = 9   # b = 0001 0001

    print("NOT a: ", ~a)
    print("a AND b: ", a & b)
    print("a OR b: ", a | b)
    print("a XOR b: ", a ^ b)
    


