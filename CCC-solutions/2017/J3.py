if __name__ == '__main__':
    startX, startY = map(int, input().split())
    destX, destY = map(int,input().split())
    units = int(input().strip())
    dist = abs(destX - startX) + abs(destY - startY)

    if units < dist or (units - dist) % 2 == 1:
        print("N")
    else:
        print("Y")

