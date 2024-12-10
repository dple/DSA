if __name__ == '__main__':
    L = int(input())
    lst = []
    for _ in range(L):
        i, c = input().split()
        lst.append(int(i)*c)

    for line in lst:
        print(line)

