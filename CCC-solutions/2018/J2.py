if __name__ == '__main__':
    N = int(input().strip())
    yesterday = input().strip()
    today = input().strip()

    occuppied = 0
    for i in range(N):
        if yesterday[i] == 'C' and today[i] == 'C':
            occuppied += 1

    print(occuppied)
