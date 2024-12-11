"""
Check if a string is a subsequence in another given string

For example:
Ref. string: hackerrank
hereiamstackerrank -> YES
hackerworld         -> NO
"""

def isSubString(ref, str):

    i, j = 0, 0
    for c in str:
        if c.lower() == ref[i]:
            i += 1
        if i == 10:
            break

    if i != 10:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    print(isSubString('hackerrank', 'hereiamstackerrank'))
