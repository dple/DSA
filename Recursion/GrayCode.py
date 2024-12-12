"""
Convert Binary to GrayCode and vice visa using recursion. 

Given the Binary code of a number as a decimal number, i.e., 1001 (decimal) but represent for 9
"""

# Time complexity: O(log n). Space O(1)
def bin2gray(n):
    if not(n):
        return 0
    
    a = n % 10
    b = int(n /10) % 10

    if (a and not(b)) or (b and not(a)):
        return (1 + 10*bin2gray(int(n / 10)))
    else:
        return 10 * bin2gray(int(n / 10))
    
    
if __name__ == '__main__':
    n = 1001        # decimal number but represent for binary number, i.e., n = 9 in actual decimal representation
    
    print("Binary string of the original number: ", n)
    gray = bin2gray(n)
    print("Gray code of ", n, "is: ", gray)    