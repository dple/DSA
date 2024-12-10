if __name__ == '__main__':
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyzz"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    word = input().strip()

    retword = ''

    for c in word:
        if c in vowels:
            retword += c
        elif c in consonants:
            retword += c    # add consonant itself
            # add a vowel
            index = alphabet.rfind(c)
            if index > 17:
                retword += 'u'
            elif index > 11:
                retword += 'o'
            elif index > 6:
                retword += 'i'
            elif index > 2:
                retword += 'e'
            else:
                retword += 'a'
            # add consonant
            index = consonants.rfind(c)
            retword += consonants[index + 1]

    print(retword)