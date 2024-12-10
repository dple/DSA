if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    if X > 0 and Y > 0:
        print(1)
    if X < 0 and Y > 0:
        print(2)
    if X < 0 and Y < 0:
        print(3)
    if X > 0 and Y < 0:
        print(4)
