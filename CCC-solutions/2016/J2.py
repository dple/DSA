if __name__ == '__main__':
    T = []
    for i in range(4):
        T.insert(i, map(int, input().split()))

    total = sum(T[0])

    for i in range(4):
        if sum(T[i]) != total or sum(T[j][i] for j in range(4)) != total:
            print("not magic")
            quit()

    print("magic")


