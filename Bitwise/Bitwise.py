
# Unset/Clear a bit, i.e., bit 1-->0
def unset_bit(num, pos):
    return num & (~(1 << pos))

# Toggle a bit at a specific position, i.e., bit 1-->0, 0 --> 1
def toggle_bit(num, pos):
    return num ^ ((1 << pos))

def set_bit(num, pos):
    bit = num & (1 << pos) >> pos
    if bit != 0:    # toggle if the bit is 0
        return num ^ (1 << pos)
    
    return num 

# Get a bit of n at a specific position 
def get_bit(num, pos):
    return (num & (1 << pos)) >> pos

# Get n bits from pos to the left
def get_n_bits(num, pos, n):
    s = '1'* n
    k = int(s, 2)
    return (num & (k << pos)) >> pos

# Relace n bits of num from position pos by a value of n bits
def replace_n_bits(num, value, pos, n):
    s_num = format(num, 'b')
    s_value = format(value, 'b')

    if len(s_value) > n:
        print("Number of bits of replaced value is bigger than", n)
        return 
    
    if len(s_value) < n:
        s_value = '0'*(n - len(s_value)) + s_value

    for _ in range(n):
         

# Check if a number is a power of two 
def is_power_two(num):
    # First num in the below expression is for the case when num is 0
    return num and (not num & (num - 1))

# Get Hamming weight of a number, i.e., number of bits '1'
def hamming_weight(n):
    hw = 0

    while n > 0:
        hw += n & 1
        n >>= 1
    
    return hw 

# Get the Hamming Distance of two given numbers 
def hamming_distance(n, m):
    
    return hamming_weight(n ^ m)

# Add two bit strings, e.g., "1100011" + "10", result is "1100101"
# Using built-in functions format() and int()
def add_two_bit_strings(s_a, s_b):
    return format(int(s_a, 2) + int(s_b, 2), 'b')


# Rotate k bits of a number n
def left_rotate(n, k):

    return (n << k) | (n >> (INT_BTIS - k))

def right_rotate(n, k):

    return (n >> k) | ((n % (1 << k)) << INT_BTIS - k) #(n >> k)|(n << (INT_BTIS - k)) & 0xFF (8 bits '1')

# Smallest power of 2 greater than or equal to n
def find_smallest_power_of_two(n):

    i = INT_BTIS - 1  
    
    while not(n >> i) and (i > 0):        
        i -= 1
    
    return 1 << i + 2


# Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number. 
def modulo_power_two(n, d):
    mask = d - 1
    return n & mask 

if __name__ == '__main__':
    INT_BTIS = 8
    a = 15   # a = 0000 1111
    b = 29   # b = 0001 1101
    print("Binary of a:", format(a, 'b'))
    print("Smallest power of 2 greater than b is:", find_smallest_power_of_two(b))
    print("Left rotate 3 bits of a:", format(left_rotate(a, 3), 'b'))
    print("Binary of b:", format(b, 'b'))
    print("Right rotate 3 bits of b:", format(right_rotate(b, 3), 'b'))
    print("b modulo power of 4^2: ", modulo_power_two(b, 16))
    print("NOT", format(a, 'b'), ": ", format(~a, 'b'))
    print(format(a, 'b'), " AND ", format(b, 'b'), ": ", format(a & b, 'b'))
    print(format(a, 'b'), " OR ", format(b, 'b'), ": ", format(a | b, 'b'))
    print(format(a, 'b'), " XOR ", format(b, 'b'), ": ", format(a ^ b, 'b'))

    print("Hamming weight of a: ", hamming_weight(a))
    print("Hamming Distance of (a, b):", hamming_distance(a, b))

    n = 123
    bit_pos = 1
    print("Binary representation of ", n, "is: ", format(n, 'b'))
    print("Bit ", bit_pos, "th of ", n, "is ", get_bit(n, bit_pos))    
    print("Clear bit at the position ", bit_pos, ":", unset_bit(n, bit_pos))
    


