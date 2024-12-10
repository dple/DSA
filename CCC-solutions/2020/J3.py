if __name__ == '__main__':
    N = int(input())        # number of drops of paints
    minX, minY, maxX, maxY = 100, 100, 0, 0
    
    for _ in range(N):
        X, Y = map(int,input().split(','))
        if X < minX:
            minX = X
        if Y < minY:
            minY = Y
        if X > maxX:
            maxX = X
        if Y > maxY:
            maxY = Y

    print(minX - 1,end="")
    print(',',end="")
    print(minY - 1)

    print(maxX + 1, end="")
    print(',', end="")
    print(maxY + 1)