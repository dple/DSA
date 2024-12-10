if __name__ == '__main__':
    N = int(input().strip())
    spcice = 0
    for _ in range(N):
        str = input().strip()
        if str == "Poblano":
            spcice += 1500
        elif str == "Mirasol":
            spcice += 6000
        elif str == "Serrano":
            spcice += 15500
        elif str == "Cayenne":
            spcice += 40000
        elif str == "Thai":
            spcice += 75000
        else:
            spcice += 125000

    print(spcice)