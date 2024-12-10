if __name__ == '__main__':
    scores = [0, 0]
    for i in range(2):
        shots = int(input())
        fields = int(input())
        frees = int(input())
        scores[i] = shots*3 + fields*2 + frees

    if scores[0] > scores[1]:
        print("A")
    elif scores[0] < scores[1]:
        print("B")
    else:
        print("T")