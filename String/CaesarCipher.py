"""
This script implements the Caesar cipher
Caesar's cipher performs a rotation shift for each letter by a number of letters.
"""

def encrypt(plain, k):
    """ Given a plain text and a number k. This implements Caesar cipher by performing a rotation shift by k position """
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ret = ''

    for c in plain:
        if c in lower:
            ret += lower[(lower.index(c) + k) % 26]
        elif c in upper:
            ret += upper[(upper.index(c) + k) % 26]
        else:
            ret += c
    return ret

def decrypt(cipher, k):
    return encrypt(cipher, -k)

if __name__ == '__main__':
    s = 'Always look on the Bright Side of Life!'
    k = 3
    cipher = encrypt(s, k)
    print("Encrypted message:", cipher)
    print("Decrypted message:", decrypt(cipher, k))


