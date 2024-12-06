import sys

#CHAR_BTIS = 8
INT_BITS = sys.getsizeof(int())
#INT_BITS = CHAR_BTIS * INT_BYTES

class bitwise:
    def __init__(self, n):
        self.x = n

    # Unset/Clear a bit, i.e., bit 1-->0
    def unset_bit(self, pos):
        self.x &= (~(1 << pos))

    def unset_n_bits(self, pos, n):
        mask = ~(((1 << n) - 1) << pos)
        self.x &= mask 

    # Toggle a bit at a specific position, i.e., bit 1-->0, 0 --> 1
    def toggle_bit(self, pos):
        self.x ^= ((1 << pos))

    def toggle_n_bits(self, pos, n):
        mask = ((1 << n) - 1) << pos
        self.x ^= mask 

    def set_bit(self, pos):
        self.x |= (1 << pos) 

    def set_n_bits(self, pos, n):
        mask = ((1 << n) - 1) << pos
        self.x |= mask 

    # Get a bit of n at a specific position 
    def get_bit(self, pos):
        return (self.x >> pos) & 1

    # Get n bits from pos to the left
    def get_n_bits(self, pos, n):        
        return (self.x >> pos) & ((1 << n) - 1)


    # Check if a number is a power of two 
    def is_power_two(self):
        # First num in the below expression is for the case when num is 0
        return self.x and (not self.x & (self.x - 1))

    # Get length in bits of a number, counting from bit '1' of the MSB
    def length(self):
        count = 0
        num = self.x

        while num > 0:
            count += 1
            num >>= 1
        
        if count == 0:
            return 1
        
        return count

    # Get Hamming weight of a number, i.e., number of bits '1'
    def hamming_weight(self):
        hw = 0
        n = self.x 

        while n > 0:
            hw += n & 1
            n >>= 1
        
        return hw 

    # Get the Hamming Distance of two given numbers 
    def hamming_distance(self, y):
        
        return self.hamming_weight(bitwise(self.x ^ y))

    # Rotate k bits of a number n
    def left_rotate(self, k):
        return (self.x << k) | (self.x >> (INT_BITS - k))

    def right_rotate(self, k):
        return (self.x >> k) | ((self.x % (1 << k)) << INT_BITS - k) #(n >> k)|(n << (INT_BTIS - k)) & 0xFF (8 bits '1')

    # Smallest power of 2 greater than or equal to n
    def find_smallest_power_of_two(self):
        i = INT_BITS - 1  
                
        n = self.x 
        if (n and not(n & (n - 1))):
            return n

        pos = 0
        while (n > 0):        
            n >>= 1
            pos += 1
        
        return 1 << pos 


    # Compute n modulo d without division(/) and modulo(%) operators, where d is a power of 2 number. 
    def modulo_power_two(self, d):
        return self.x & (d - 1) 

    # Relace n bits of num from position pos by a value of n bits
    # Using string 
    def replace_n_bits_string(self, value, pos, n):
        s_num = format(self.x, 'b')    
        s_value = format(value, 'b')


        if len(s_value) > n:
            print("Number of bits of replaced value is bigger than", n)
            return 
        
        if len(s_value) < n:
            s_value = '0'*(n - len(s_value)) + s_value
            
        if pos + n > len(s_num):
            s_num = '0' * (pos + n - len(s_num)) + s_num
        
        print("Original number: ", s_num)   
        print("Replaced number: ", s_num[:len(s_num) - pos - n]  + s_value + s_num[len(s_num) - pos:])
         
    # Relace n bits of num from position pos by a value of n bits
    # Using bitwise operations (shift)
    def replace_n_bits(self, value, pos, n):        
        s_value = format(value, 'b')


        if len(s_value) > n:
            print("Number of bits of replaced value is bigger than", n)
            return 
        
        lower = self.x & ((1 << pos) - 1)
        print("Lower: ", format(lower, 'b'))

        upper = self.x >> (pos + n)
        print("Upper: ", format(upper, 'b'))

        print("Original number: ", format(self.x, 'b'))   
        self.x = (((upper << n) + value) << pos) + lower
        print("Replaced number: ", format(self.x, 'b'))
        
    # Using XOR 
    def replace_n_bits_xor(self, value, pos, n):
       
        print("Original number: ", format(self.x, 'b'))   
        
        sub = (self.x >> pos) & ((1 << n) - 1)
        xor = value ^ sub 
        self.x ^= xor << pos 
        
        print("Replaced number: ", format(self.x, 'b'))

if __name__ == '__main__':
    
    bw = bitwise(47)    
    bw.replace_n_bits_xor(7, 2, 3)
    print(INT_BITS - 1)
    print(bw.is_smaller(64))

    """
    
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
    """


# Add two bit strings, e.g., "1100011" + "10", result is "1100101"
# Using built-in functions format() and int()
def add_two_bit_strings(s_a, s_b):
    return format(int(s_a, 2) + int(s_b, 2), 'b')
