if __name__ == '__main__':
    N = int(input().strip())
    shift = int(input().strip())

    sum = N
    for _ in range(shift):
        N *= 10
        sum += N

    print(sum)