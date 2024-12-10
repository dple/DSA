if __name__ == '__main__':
    max = 1
    word = input().strip()
    l = len(word)

    for i in range(l):
        for j in range(l, 0, -1):
            subword = word[i:j]
            if subword == subword[::-1]:
                if max < j - i:
                    max = j - i
                break
    print(max)