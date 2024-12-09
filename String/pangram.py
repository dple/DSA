"""
A pangram is a string that contains every letter of the alphabet.
Given a sentence determine whether it is a pangram in the English alphabet.
Return either pangram or not pangram as appropriate.

For example:
Input: We promptly judged antique ivory buckles for the next prize
Output: pangram
"""

def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    states = 26*[0]
    for c in s:
        if c.lower() in alphabet:
            states[alphabet.index(c.lower())] = 1
    for i in range(26):
        if states[i] == 0:
            return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    s= 'We promptly judged antique ivory buckles for the next prize'
    print(pangrams(s))