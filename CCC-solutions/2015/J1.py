if __name__ == '__main__':
    month = int(input().strip())
    day = int(input().strip())

    if month > 2:
        print("After")
    elif month < 2:
        print("Before")
    elif day > 18:
        print("After")
    elif day < 18:
        print("Before")
    else:
        print("Special")