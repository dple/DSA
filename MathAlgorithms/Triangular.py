import math 

# Determine of a number is triangular
def isTriangular(num):
    k = int(math.sqrt(2*num))
    if num == k *(k + 1)/2:
        return True
    else:
        return False
    
if __name__ == '__main__':
    num = 55
    if (isTriangular(num)):
        print(num, " is a triangular number")
    else:
        print(num, " is NOT a triangular number")