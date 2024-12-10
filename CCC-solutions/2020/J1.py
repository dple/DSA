if __name__ == '__main__':
    S = int(input())            # number of small treats
    M = int(input())            # number of medium treats
    L = int(input())            # number of large treats

    happy_scores = S + 2*M + 3*L
    if happy_scores >= 10:
        print("happy")
    else:
        print("sad")