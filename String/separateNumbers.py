"""
Separate the Numbers: Given a string, check if it can be split into a sequence of increasing numbers.

For example:
- s = '1234' can be split into a sequence 1, 2, 3, 4
- s = '910111213' can be split into a sequence 9, 10, 11, 12, 13
- s = '99100101102103' can be split into a sequence 99, 100, 101, 102, 103
- s = '102304' can be be split as above
"""

def separateNumbers(s):
    n = len(s)
    for i in range(1, n//2 + 1):
        stringx = s[:i]        
        start = int(stringx)
        x = start
        while len(stringx) < n:
            x += 1
            stringx += str(x)
        if stringx == s:
            print('YES {}'.format(start))
            return

    print('NO')

if __name__ == '__main__':
    separateNumbers('99100101102103')
    separateNumbers('9101112103')
