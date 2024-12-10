if __name__ == '__main__':
    c = 0
    for _ in range(6):
        if input().strip() == 'W':
            c += 1

    if c >= 5:
        print('1')
    elif c >= 3:
        print('2')
    elif c >= 1:
        print('3')
    else:
        print('-1')

