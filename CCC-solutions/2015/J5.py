def solver(n, k, m):
    if n == k or k == 1:
        return 1

    if (n, k, m) in states:
        return states[(n, k, m)]

    count = 0
    for i in range(m, n // k + 1):
        count += solver(n - i, k - 1, i)

    states[(n, k, m)] = count

    return count


if __name__ == '__main__':
    n = int(input().strip())            # number of pieces
    k = int(input().strip())            # number of people

    states = {}
    if n < k:
        print('0')
        exit()

    print(solver(n, k, 1))
