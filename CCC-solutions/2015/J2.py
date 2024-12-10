if __name__ == '__main__':
    str = input().strip()
    happy = len(str.split(":-)")) - 1
    sad = len(str.split(":-(")) - 1

    if happy == 0 and sad == 0:
        print("none")
    elif happy == sad:
        print("unsure")
    elif happy > sad:
        print("happy")
    else:
        print("sad")