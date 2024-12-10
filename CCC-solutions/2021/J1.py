# Bloiling water

if __name__ == '__main__':
    B = int(input())        # get the temperature the water is boiling
    P = 5*B - 400           # Atmostpheric pressure
    print(P)                #

    if (P > 100):           # Below sea level
        print("-1")
    elif (P == 100):        # Sea level
        print("0")
    else:                   # Above sea level
        print("1")
