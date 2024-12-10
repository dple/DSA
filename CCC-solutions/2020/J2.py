# Epidemiology

if __name__ == '__main__':
    P = int(input())            # threshold number of people having disease
    N = int(input())            # number of people having disease on Day 0
    R = int(input())            # infected rate

    day = 0
    total = N
    last = N
    while total <= P:
        new = last * R
        total += new
        last = new
        day += 1

    print(day)