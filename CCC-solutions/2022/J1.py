# Cup cakes
if __name__ == '__main__':
    n_students = 28     # number of students in the class
    R = int(input())    # get number of big boxes
    S = int(input())    # get number of small boxes
    n_cupcakes = R*8 + S*3

    print(n_cupcakes - n_students)  # Output the cupcakes leftover