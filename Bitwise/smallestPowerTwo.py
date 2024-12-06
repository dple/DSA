def find_smallest_power_of_two(n):
    if (n and  not (n & (n - 1))):         
        return n
    
    pos = 0
    while n > 0:
        n >>= 1
        pos += 1
    
    return (1 << pos)
    